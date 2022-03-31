from datetime import datetime
from pathlib import Path

from lib_bgp_simulator import Graph, Simulator, ROVAS, MPMethod

# LITE
from .as_classes import ROVPPV1LiteSimpleAS
from .as_classes import ROVPPV2LiteSimpleAS
from .as_classes import ROVPPV2aLiteSimpleAS
from .as_classes import ROVPPV2ShortenLiteSimpleAS

# NON LITE
from .as_classes import ROVPPV1SimpleAS
from .as_classes import ROVPPV2SimpleAS
from .as_classes import ROVPPV2aSimpleAS
from .as_classes import ROVPPV2ShortenSimpleAS
from .as_classes import ROVPPV3AS

# Attacks
from .engine_input import ROVPPSubprefixHijack
from .engine_input import ROVPPNonRoutedSuperprefixHijack
from .engine_input import ROVPPSuperprefixPrefixHijack
from .engine_input import ROVPPPrefixHijack
from .engine_input import ROVPPNonRoutedPrefixHijack

default_kwargs = {"percent_adoptions": [0, 20, 60],
                  "num_trials": 1}


def run_sim(graph, path):
    sim = Simulator(parse_cpus=8)

    sim.run(graphs=[graph], graph_path=path, mp_method=MPMethod.SINGLE_PROCESS)


def main():
    assert isinstance(input("Turn asserts off for speed?"), str)

    # Get's all of the general graphs for all types of attacks
    atk = ROVPPNonRoutedPrefixHijack
    pols = (ROVPPV2aSimpleAS, ROVPPV2SimpleAS)
    kwargs = {"EngineInputCls": atk, **default_kwargs}
    graph = Graph(adopt_as_classes=pols, **kwargs)
    run_sim(graph, Path(f"/home/anon/v2a_check_graphs.tar.gz"))
    print(f"Completed {atk}")

if __name__ == "__main__":
    start = datetime.now()
    main()
    print((datetime.now() - start).total_seconds())
