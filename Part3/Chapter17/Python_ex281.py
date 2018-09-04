import re

text = """Fortunately, the embarrassment that my
maculate __APPEARANCE MIGHT CAUSE__ was evitable.
There were two ways about it, but the chances
that __SOMEONE AS FLAPPABLE__ as I would be ept enough
to __BECOME PERSONA GRATA__ or a sung hero were slim.
I was, after all, something to sneeze at, someone
you could easily hold a candle to, someone who
usually aroused bridled passion.

So __I DECIDED NOT TO RISK__ it. But then, all at once,
for some apparent reason, she looked in my
direction and smiled in a way that I could
make heads or tails of.
"""

def mad_libs(mls):
    """
    :param mls: In the string user input need to be arounded
    with double underscore. You can't paste underscore to hint:
    __hint_hint__ (can not);
    __hint__(you can)
    """
    hints = re.findall("__.*?__", mls)

    if hints is not None:
        for word in hints:
            new = input("Enter {} ".format(word))
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("error of input")


mad_libs(text)
    
