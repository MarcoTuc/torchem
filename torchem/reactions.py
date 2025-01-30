class AbstractReaction:
    pass

class SimpleReaction(AbstractReaction):
    
    def __init__(
            self,
            reagents: list[str],
            products: list[str],
            fwd_rate: float,
            bwd_rate: float
            ):
        self.reagents = reagents # set of reagents
        self.products = products # set of products
        self.fwd = fwd_rate # forward reaction rate  R -> P
        self.bwd = bwd_rate # backward reaction rate R <- P

