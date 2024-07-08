from IPython.core.magic import Magics, magics_class, cell_magic
from IPython import get_ipython

@magics_class
class EchoMagics(Magics):
    @cell_magic
    def echo_append(self, line, cell):
         exec(cell + '\nprint("Success!")')

def load_ipython_extension(ipython):
    ipython.register_magics(EchoMagics)
