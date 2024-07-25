from IPython.core.magic import Magics, magics_class, cell_magic
from IPython import get_ipython


@magics_class
class EchoMagics(Magics):
    def __init__(self, *args, **kwargs):
        self.echo_string = ""
        super().__init__(*args, **kwargs)

    @cell_magic
    def echo_append(self, line, cell):
        self.echo_string += cell + '\n'
        exec(self.echo_string + '\nprint("Success!")')


def load_ipython_extension(ipython):
    ipython.register_magics(EchoMagics)





