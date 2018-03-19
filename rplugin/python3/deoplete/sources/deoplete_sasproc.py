#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from .base import Base

PROCEDURES = [
        "access", "aceclus", "adaptivereg", "allele", "anom", "anova", "append", "arima", "authlib", "autoreg", "bom", "boxplot", "btl", "calendar", "calis", "callrfc", "cancorr", "candisc", "capability", "casecontrol", "catalog", "catmod", "chart", "cimport", "clp", "cluster", "compare", "computab", "contents", "convert", "copy", "corr", "corresp", "countreg", "cpm", "cport", "cusum", "data", "datasets", "datasource", "dbf", "dbload", "define_event", "define_tagset", "delete", "dif", "discrim", "display", "distance", "document", "dqmatch", "dqscheme", "dqsrvadm", "dqsrvsvc", "ds2", "dstrans", "dtree", "entropy", "esm", "expand", "explode", "export", "factex", "factor", "family", "fastclus", "fcmp", "fedsql", "fmm", "fontreg", "forecast", "format", "forms", "freq", "fsbrowse", "fsedit", "fsletter", "fslist", "fsview", "g3d", "g3grid", "ga", "gam", "ganno", "gantt", "gareabar", "gbarline", "gchart", "gcontour", "gdevice", "geneselect", "genmod", "geocode", "gfont", "gimport", "ginside", "gkeymap", "gkpi", "glimmix", "glm", "glmmod", "glmpower", "glmselect", "gmap", "goptions", "gplot", "gproject", "gradar", "greduce", "gremove", "greplay", "groovy", "gslide", "gtestit", "gtile", "hadoop", "haplotype", "hp4score", "hpbin", "hpclus", "hpcorr", "hpcountreg", "hpdecide", "hpdmdb", "hpds2", "hpf", "hpfarimaspec", "hpfdiagnose", "hpfengine", "hpfesmspec", "hpfevents", "hpfexmspec", "hpfidmspec", "hpforest", "hpfselect", "hpfucmspec", "hpgenselect", "hpimpute", "hplmixed", "hplogistic", "hplso", "hpmixed", "hpneural", "hpnlin", "hpnlmod", "hpqlim", "hpreduce", "hpreg", "hpsample", "hpseverity", "hpsplit", "hpsummary", "hptmine", "hptmscore", "htsnp", "http", "iml", "import", "imstat", "inbreed", "infomaps", "intpoint", "ishikawa", "json", "kde", "krige2d", "lattice", "lifereg", "lifetest", "loan", "loess", "logistic", "lp", "macontrol", "macro", "mapimport", "mcmc", "mdc", "mds", "means", "metadata", "mi", "mianalyze", "migrate", "mixed", "modeclus", "model", "multtest", "nested", "netdraw", "netflow", "nlin", "nlmixed", "nlp", "npar1way", "ods", "olap", "operate", "optex", "optgraph", "options", "optload", "optlp", "optmilp", "optmodel", "optqp", "optsave", "orthoreg", "panel", "pareto", "pdlreg", "phreg", "plan", "plm", "plot", "pls", "pm", "pmenu", "power", "presenv", "princomp", "prinqual", "print", "printto", "probit", "proto", "prtdef", "prtexp", "psmooth", "pwencode", "qdevice", "qlim", "quantlife", "quantreg", "quantselect", "rank", "reg", "registry", "reliability", "report", "robustreg", "rsreg", "scaproc", "score", "seqdesign", "seqtest", "server", "severity", "sgdesign", "sgpanel", "sgplot", "sgrender", "sgscatter", "shewhart", "sim2d", "similarity", "simlin", "simnormal", "soap", "sort", "spectra", "sql", "standard", "statespace", "statgraph", "stdize", "stdrate", "stepdisc", "stp", "stream", "summary", "surveyfreq", "surveylogistic", "surveymeans", "surveyphreg", "surveyreg", "surveyselect", "syslin", "tabulate", "tcalis", "template", "timeid", "timeplot", "timeseries", "tpspline", "trans", "transpose", "transreg", "trantab", "tree", "tscsreg", "ttest", "ucm", "univariate", "varclus", "varcomp", "variogram", "varmax", "x11", "x12", "xsl"
        ]


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'sasProc'
        self.mark = '[sasProc]'
        self.filetypes = ['sas']
        self.min_pattern_length = 2
        self.rank = 500
        self.input_pattern = r'^(?:proc|PROC)\s'
        self.keywords = [{'word': x} for x in PROCEDURES]

    def on_init(self, context):
        self.complete_pos = re.compile(r'(?<=(?:proc|PROC)\s)\w*$')

    def get_complete_position(self, context):
        m = self.complete_pos.search(context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        return self.keywords
