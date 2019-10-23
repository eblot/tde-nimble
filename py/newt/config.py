from collections import defaultdict
from copy import deepcopy
from logging import getLogger
from os import environ, rename, walk
from os.path import (basename, dirname, isdir, join as joinpath, normpath,
                     relpath)
from pprint import pformat
from re import compile as recompile
from typing import Mapping, TextIO
from ruamel.yaml import YAMLObject, load_all as yaml_load
from ruamel.yaml.constructor import ConstructorError
from ruamel.yaml.loader import Loader
from ruamel.yaml.parser import ParserError


class NewtError(RuntimeError):
    """Base class for Newt errors."""


class NewtConfigParser:
    """
    """

    NEWT_CRE = recompile(r'MYNEWT_VAL(\()?(_)?(.*)(?(1)\))')

    def __init__(self, debug):
        self.log = getLogger('tde.newt.config')
        self._debug = debug
        self._syscfgs = {}
        self._pkgs = {}
        self._syscfg = {}
        self._defs = {}
        self._inits = []

    def scan(self, topdir: str) -> None:
        if not isdir(topdir):
            raise NewtError(f'No such directory: {topdir}')
        for dirpath, dirnames, filenames in walk(topdir):
            dirnames[:] = [dn for dn in dirnames if not dn.startswith('.')]
            for fn in filenames:
                if not fn.endswith('.yml'):
                    continue
                filename = normpath(joinpath(dirpath, fn))
                if fn == 'syscfg.yml':
                    with open(filename, 'rt') as yfp:
                        self._syscfgs.update(self._parse(yfp))
                if fn == 'pkg.yml':
                    with open(filename, 'rt') as yfp:
                        self._pkgs.update(self._parse(yfp))
        self._build_syscfg()
        self._build_pkg()

    def _parse(self, yamlfp: TextIO) -> dict:
        ydefs = yaml_load(yamlfp, Loader=Loader)
        modname = dirname(yamlfp.name)
        contents = {}
        try:
            for ydef in ydefs:
                if not isinstance(ydef, dict):
                    raise NewtError(f'Unexpected config format in '
                                    f'{yamlfp.name}')
                top = {}
                prev = []
                for ykey, yval in ydef.items():
                    source = top
                    while True:
                        kparts = ykey.split('.', 1)
                        if len(kparts) == 1:
                            if not isinstance(source, dict) and prev:
                                source = prev[0][prev[1]] = \
                                    {'': prev[0][prev[1]]}
                            source[ykey] = yval
                            break
                        if kparts[0] not in source:
                            source[kparts[0]] = {}
                        prev = source, kparts[0]
                        source, ykey = source[kparts[0]], kparts[1]
                contents[modname] = top
            return contents
        except (ParserError, ConstructorError) as exc:
            raise NewtError(f'Invalid configuration: {exc}')

    def _build_pkg(self):
        inits = self._get(self._build(self._pkgs), 'pkg.init')
        cinits = {}
        for name, value in inits.items():
            if isinstance(value, dict):
                continue
            cinits[name] = self._resolve(value)
        self._inits.clear()
        for func in sorted(cinits, key=lambda f: cinits[f]):
            self._inits.append(func)
        print('void sysinit_app(void);')
        print()
        for func in self._inits:
            print(f'void {func}(void);')
        print()
        print('void sysinit_app(void)')
        print('{')
        for func in self._inits:
            print(f'   {func}();')
        print('}')

    def _build_syscfg(self):
        self._syscfg = self._build(self._syscfgs, 'deprecated')
        self._defs = self._get(self._syscfg, 'syscfg.defs')

    @classmethod
    def _get(cls, items, path):
        for pth in path.split('.'):
            try:
                items = items[pth]
            except KeyError:
                return {}
        return items

    def _resolve(self, name):
        value = self._defs
        while isinstance(value, dict):
            if name not in value:
                break
            name = value[name]
            if isinstance(name, (list, dict)):
                self.log.warning('Cannot resolve %s', name.__class__.__name__)
                break
        return name

    def _build(self, items, *keywords):
        def cleanup(obj):
            if not isinstance(obj, dict):
                return obj
            for keyword in keywords:
                if keyword in obj:
                    return None
            cobj = {}
            for okey, oval in obj.items():
                if okey in {'description', }:
                    continue
                value = cleanup(oval)
                if value is not None:
                    if (isinstance(value, dict) and
                            len(value) == 1 and
                            'value' in value):
                        value = value.pop('value')
                    if isinstance(value, str) and value:
                        value = self.NEWT_CRE.sub(r'\3', value)
                    cobj[okey] = value
            return cobj
        output = {}
        for val in items.values():
            val = cleanup(val)
            output = self.merge_containers(output, val, True)
        return output

    def merge_containers(self, obj_a, obj_b, ignore_error: bool = False):
        """Recursively merge dictionaries.

           from https://stackoverflow.com/questions/38987/\
                   how-do-i-merge-two-dictionaries-in-a-single-expression
        """
        def desc(obj):
            if isinstance(obj, (list, dict)):
                return obj.__class__.__name__
            return obj
        if isinstance(obj_a, list):
            list_c = []
            list_c.extend(obj_a)
            if isinstance(obj_b, list):
                list_c.extend(obj_b)
            elif obj_b is not None:
                list_c.append(obj_b)
            return list_c
        if isinstance(obj_a, dict):
            if obj_b is None:
                return deepcopy(obj_a)
            dict_c = {}
            try:
                overlapping_keys = obj_a.keys() & obj_b.keys()
            except AttributeError:
                msg = f'[{desc(obj_a)} + {desc(obj_b)}]: merge failure'
                if ignore_error:
                    self.log.error(msg)
                    return deepcopy(obj_a)
                else:
                    raise ValueError(msg)
            for key in overlapping_keys:
                try:
                    dict_c[key] = self.merge_containers(obj_a[key], obj_b[key],
                                                        ignore_error)
                except ValueError as exc:
                    raise ValueError(f'{key}.{exc}')
            for key in obj_a.keys() - overlapping_keys:
                dict_c[key] = deepcopy(obj_a[key])
            for key in obj_b.keys() - overlapping_keys:
                dict_c[key] = deepcopy(obj_b[key])
            return dict_c
        return obj_b

