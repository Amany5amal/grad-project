pip install gspan_mining
from gspan_mining.config import parser
from gspan_mining.main import main
%pylab inline
args_str = '-s 2 -d True -l 5 -p True -w True Chemical_340.txt'
FLAGS, _ = parser.parse_known_args(args=args_str.split())
gs = main(FLAGS)
for g in gs.graphs.values():
    g.plot()
