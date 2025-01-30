import jax.numpy as jnp

from reactions import AbstractReaction, SimpleReaction


class ReactionSystem:
    
    def __init__(
            self,
            **kwargs
            ):
        
        for key, arg in kwargs.items(): 
            setattr(self, key, arg)

    def set_stochiometry(self, S: jnp.Array):
        """ Initialize the stochiometric matrix """
        self.S = S

    def set_species(self, species: list[str]):
        self.species = species

    def set_reactions(self, reactions: list[AbstractReaction]):
        self.reactions = reactions

    