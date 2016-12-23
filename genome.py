"""Classes for storing genetic information about an organism.
Currently planned to only handle two parent selection.
"""


class Genome(object):
    """Exposes the genotype information of an organism."""

    def __init__(self, genome_a, genome_b):
        """Create Genome from parents' genomes."""
        self.chromosomes = (genome_a.get_gamete_chromosomes
                            + genome_b.get_gamete_chromosomes)

    def get_gamete_chromosomes(self):
        """Conduct chromosome recombination to produce new unique versions."""
        left_side = []
        right_side = []
        unsided = self.chromosomes.copy()
        # TODO Shuffle self.chromosomes before use
        for chromosome_a in self.chromosomes:
            if chromosome_a in unsided:
                unsided.remove(chromosome_a)


class Chromosome(object):
    """Object for storing fragments of parents' genomes."""

    def __init__(self, genome):
        """Create a chromosome by shuffling the chromosomes in the genome."""
        self.signature = None


class Gene(object):
    """Contains phenotype and genotype for a specific gene."""

    def __init__(self):
        self.effects = {}
