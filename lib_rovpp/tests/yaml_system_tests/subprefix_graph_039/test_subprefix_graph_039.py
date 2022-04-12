from pathlib import Path

from lib_bgp_simulator import BaseGraphSystemTester, BGPSimpleAS, Graph039
from lib_bgp_simulator import enums

from ..unstable import Unstable
from ....as_classes import ROVPPV1SimpleAS, ROVPPV1LiteSimpleAS
from ....as_classes import ROVPPV2SimpleAS, ROVPPV2LiteSimpleAS

from ....engine_input import ROVPPSubprefixHijack


class BaseSubprefixGraph039Tester(Unstable, BaseGraphSystemTester):
    GraphInfoCls = Graph039
    BaseASCls = BGPSimpleAS
    EngineInputCls = ROVPPSubprefixHijack
    base_dir = Path(__file__).parent
    adopting_asns = (enums.ASNs.VICTIM.value, 33,)


class Test130(BaseSubprefixGraph039Tester):
    AdoptASCls = ROVPPV1SimpleAS


class Test131(BaseSubprefixGraph039Tester):
    AdoptASCls = ROVPPV2SimpleAS


class Test132(BaseSubprefixGraph039Tester):
    AdoptASCls = ROVPPV1LiteSimpleAS


class Test133(BaseSubprefixGraph039Tester):
    AdoptASCls = ROVPPV2LiteSimpleAS
