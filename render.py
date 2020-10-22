from model import model

from pysb.tools import render_reactions

print(render_reactions.run(model))
