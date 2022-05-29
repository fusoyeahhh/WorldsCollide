from . import formation_flags
from .multipliers import Multipliers
from . import load_enemy_level
from . import no_exp_party_divide
from . import suplex_train_check
from . import auto_status
from . import end_checks
from .animations import Animations

__all__ = ["Battle"]
class Battle:
    def __init__(self):
        self.multipliers = Multipliers()
        self.animations = Animations()
