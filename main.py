import collections
import tqdm
# from pubmed_searchx import search_from_file
from src.pubmed_searchx import search_cmd
# pairs = [("corin", "depression")]
# output_file = "out.json"  # Set to None if do not write to file
# info_list, return_code = gene_search(pairs, authors=True, title=True,
#                                      year=True, pubmed_id=True, path_out=output_file)

gene_inp = "./gene_list.txt"
term_inp = "./term_list.txt"

# search_from_file(gene_list_path=gene_inp, term_list_path=term_inp, dir_out=".")
# aa = collections.OrderedDict([('authors', True), ('title', True), ('year', True), ('pubmed_id', True)])
# print(aa['authors'])
# for i, v in aa.items():
#     print(i, v)

search_cmd()