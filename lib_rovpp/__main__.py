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
from .engine_input import ROVPPNonRoutedSuperprefixPrefixHijack


default_kwargs = {"percent_adoptions": [0, 5, 10, 20, 30, 40, 60, 80, 100],
                  "num_trials": 1}

non_lite_policies =(ROVPPV1SimpleAS,
                    ROVPPV2SimpleAS,
                    ROVPPV2aSimpleAS,
                    # ROVPPV2ShortenSimpleAS,
                    )

rov_non_lite_rovpp = (ROVAS,) + non_lite_policies


def run_sim(graph, path):
    sim = Simulator(parse_cpus=1)

    sim.run(graphs=[graph], graph_path=path, mp_method=MPMethod.MP)


def main():

    assert isinstance(input("Turn asserts off for speed?"), str)

    # Get's all of the general graphs for all types of attacks
    for atk in [ROVPPSubprefixHijack,
                ROVPPNonRoutedSuperprefixHijack,
                ROVPPSuperprefixPrefixHijack,
                ROVPPPrefixHijack,
                ROVPPNonRoutedPrefixHijack,
                ROVPPNonRoutedSuperprefixPrefixHijack]:
        if atk == ROVPPSubprefixHijack:
            pols = rov_non_lite_rovpp + (ROVPPV3AS,)
        else:
            pols = rov_non_lite_rovpp
        kwargs = {"EngineInputCls": atk, **default_kwargs}
        graph = Graph(adopt_as_classes=pols, **kwargs)

        start = datetime.now()
        run_sim(graph, Path(f"/home/anon/{atk.__name__}_graphs.tar.gz"))
        print(f"Completed {atk}")
        print((datetime.now() - start).total_seconds())
        #print("Ending early")
        #return

    kwargs = {"EngineInputCls": ROVPPSubprefixHijack, **default_kwargs}
    graph = Graph(adopt_as_classes=[ROVPPV1LiteSimpleAS, ROVPPV1SimpleAS],
                  **kwargs)
    run_sim(graph, Path("/home/anon/v1_lite_vs_non_lite_graphs.tar.gz"))

if __name__ == "__main__":
    start = datetime.now()
    main()
    print((datetime.now() - start).total_seconds())
