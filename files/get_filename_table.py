import argparse


def make_url(dir, fname):
    return f'{{{{% staticref "files/{dir}/{fname}" "newtab" %}}}}link{{{{% /staticref %}}}}'


def make_markdown_table(array):
    """ Input: Python list with rows of table as lists
               First element as header.
        Output: String to put into a .md file

    Ex Input:
        [["Name", "Age", "Height"],
         ["Jake", 20, 5'10],
         ["Mary", 21, 5'7]]
    """

    markdown = "\n" + str("| ")

    for e in array[0]:
        to_add = " " + str(e) + str(" |")
        markdown += to_add
    markdown += "\n"

    markdown += '|'
    for i in range(len(array[0])):
        markdown += str("-------------- | ")
    markdown += "\n"

    for entry in array[1:]:
        markdown += str("| ")
        for e in entry:
            to_add = str(e) + str(" | ")
            markdown += to_add
        markdown += "\n"

    return markdown + "\n"


if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-dir', "--dir", type=str,
                        help='请输入一个文件夹地址')

    args = parser.parse_args()
    d = args.dir
    print(f"target dir: {d}")
    import os

    fnames = os.listdir(d)
    print(f"contain files: {fnames}")

    array = [["TOPIC	", "SLIDES	", "READINGS	", "DEMOS"]]

    for fname in fnames:
        array.append([fname.rstrip('.pdf'), make_url(d, fname), ' ', ' '])

    print(' ')
    print(make_markdown_table(array))
