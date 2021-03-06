"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import thinkbayes
import thinkplot


class Train(thinkbayes.Suite):
    """Represents hypotheses about how many trains the company has.

    The likelihood function for the train problem is the same as
    for the Dice problem.
    """
    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: number of trains the carrier operates
        data: the number of the observed train
        """
        # fill this in!
        if data > hypo:
            return 0
        return 1/hypo



def main():
    hypos = range(100, 1001)
    suite = Train(hypos)

    suite.Update(50)

    thinkplot.PrePlot(1)
    thinkplot.Pmf(suite)
    thinkplot.Show(xlabel='Number of trains',
                   ylabel='Probability',
                   legend=False)

    for train in [13, 45, 89, 22, 33, 35]:
        suite.Update(train)

    thinkplot.PrePlot(1)
    thinkplot.Pmf(suite)
    thinkplot.Show(xlabel='Number of trains',
                   ylabel='Probability',
                   legend=False)

    print(suite.Mean())
    print(suite.MaximumLikelihood())
    print(suite.CredibleInterval(90))

if __name__ == '__main__':
    main()
