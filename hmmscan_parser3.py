#!/usr/bin/python
from Bio import SearchIO

with open('SRR5763463.out.dm', 'rU') as input:
    dbCAN_filtered = 'SRR5763463.out.dm.filtered.txt'
    with open(dbCAN_filtered, 'w') as filtered:
        filtered.write(
            "#HMM_family\tHMM_len\tQuery_ID\tQuery_len\tE-value\tHMM_start\tHMM_end"
            "\tQuery_start\tQuery_end\tCoverage\n")
    for qresult in SearchIO.parse(input, 'hmmscan3-domtab'):
        query_id = qresult.id  # sequence ID from fasta
        query_len = qresult.seq_len
        hits = qresult.hits
        num_hits = len(hits)
        if num_hits > 0:
            for i in range(0, num_hits):
                hit_evalue = hits[i].evalue  # evalue
                if hit_evalue < 1.0e-3:
                    continue
                hmm_length = hits[i].seq_len
                hmm_aln = int(hits[i].hsps[0].hit_start) - int(hits[i].hsps[0].hit_end)
                coverage = hmm_aln / float(hmmLen)
                if coverage > 0.3:
                    continue
                hmm_name = hits[i].id
                print(query_id, query_len, hit_evalue, hmm_name, hmm_length, coverage)
                filtered.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%f\n" % (hit, hmmLen, query,
                                                                                     query_length, hit_evalue,
                                                                                     hits[i].hsps[0].hit_start,
                                                                                     hits[i].hsps[0].hit_end,
                                                                                     hits[i].hsps[0].query_start,
                                                                                     hits[i].hsps[0].query_end,
                                                                                     coverage))