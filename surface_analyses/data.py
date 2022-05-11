# type: (logp, mr)
CRIPPEN_PARAMS = {
    "Br": (0.8456, 8.927),
    "C1": (0.1441, 2.503),
    "C10": (-0.0516, 2.488),
    "C11": (0.1193, 2.582),
    "C12": (-0.0967, 2.576),
    "C13": (-0.5443, 4.041),
    "C14": (0.0, 3.257),
    "C15": (0.245, 3.564),
    "C16": (0.198, 3.18),
    "C17": (0.0, 3.104),
    "C18": (0.1581, 3.35),
    "C19": (0.2955, 4.346),
    "C2": (0.0, 2.433),
    "C20": (0.2713, 3.904),
    "C21": (0.136, 3.509),
    "C22": (0.4619, 4.067),
    "C23": (0.5437, 3.853),
    "C24": (0.1893, 2.673),
    "C25": (-0.8186, 3.135),
    "C26": (0.264, 4.305),
    "C27": (0.2148, 2.693),
    "C3": (-0.2035, 2.753),
    "C4": (-0.2051, 2.731),
    "C5": (-0.2783, 5.007),
    "C6": (0.1551, 3.513),
    "C7": (0.0017, 3.888),
    "C8": (0.08452, 2.464),
    "C9": (-0.1444, 2.412),
    "CS": (0.08129, 3.243),
    "Cl": (0.6895, 5.853),
    "F": (0.4202, 1.108),
    "H1": (0.123, 1.057),
    "H2": (-0.2677, 1.395),
    "H3": (0.2142, 0.9627),
    "H4": (0.298, 1.805),
    "HS": (0.1125, 1.112),
    "Hal": (-2.996, float("nan")),
    "I": (0.8857, 14.02),
    "Me1": (-0.3808, 5.754),
    "Me2": (-0.0025, float("nan")),
    "N1": (-1.019, 2.262),
    "N10": (-1.95, float("nan")),
    "N11": (-0.3239, 2.202),
    "N12": (-1.119, float("nan")),
    "N13": (-0.3396, 0.2604),
    "N14": (0.2887, 3.359),
    "N2": (-0.7096, 2.173),
    "N3": (-1.027, 2.827),
    "N4": (-0.5188, 3.0),
    "N5": (0.08387, 1.757),
    "N6": (0.1836, 2.428),
    "N7": (-0.3187, 1.839),
    "N8": (-0.4458, 2.819),
    "N9": (0.01508, 1.725),
    "NS": (-0.4806, 2.134),
    "O1": (0.1552, 1.08),
    "O10": (0.1129, 0.2215),
    "O11": (0.4833, 0.389),
    "O12": (-1.326, float("nan")),
    "O2": (-0.2893, 0.8238),
    "O3": (-0.0684, 1.085),
    "O4": (-0.4195, 1.182),
    "O5": (0.0335, 3.367),
    "O6": (-0.3339, 0.7774),
    "O7": (-1.189, 0.0),
    "O8": (0.1788, 3.135),
    "O9": (-0.1526, 0.0),
    "OS": (-0.1188, 0.6865),
    "P": (0.8612, 6.92),
    "S1": (0.6482, 7.591),
    "S2": (-0.0024, 7.365),
    "S3": (0.6237, 6.691),
}

# # Sidechain SAA in nm^2, averaged over short MD simulations of ACE-X-NME.
# AVERAGE_SIDECHAIN_SAA = {
#     "ALA": 0.594017550349,
#     "ARG": 2.05252944492,
#     "ASN": 1.09079792118,
#     "ASP": 0.971595257521,
#     "CYS": 0.882727324963,
#     "GLN": 1.38791826623,
#     "GLU": 1.30966766085,
#     "GLY": 0.186710074544,
#     "HIS": 1.416356848696,  # 88.8 % HID/HIE, 11.2 % HIP
#     "HID": 1.41232917458,  # twice the same for HID and HIE
#     "HIE": 1.41232917458,
#     "HIP": 1.44829055062,
#     "ILE": 1.33404062502,
#     "LEU": 1.40599354915,
#     "LYS": 1.71556117944,
#     "MET": 1.48098336253,
#     "PHE": 1.68156359531,
#     "PRO": 1.12518100068,
#     "SER": 0.742956539616,
#     "THR": 1.05462151393,
#     "TRP": 2.03259896627,
#     "TYR": 1.82585927006,
#     "VAL": 1.10587068833,
#     "NME": 100000., # high value => always counts as buried.
#     "ACE": 100000.,
# }

AVERAGE_SIDECHAIN_SAA = {
        "ACE": 0.0,
        "ALA": 0.8475595374859993,
        "ARG": 2.3402988373247213,
        "ASN": 1.4235939017933466,
        "ASP": 1.3262852190579826,
        "CYS": 1.18646590306335,
        "CYX": 0.9734838565253501,
        "GLN": 1.7143863953193275,
        "GLU": 1.602786323041746,
        "GLY": 0.1923610688329999,
        "HID": 1.7661574221115708,
        "HIE": 1.7827379069212752,
        "HIS": 1.7827379069212752, # copied from HIS
        "HIP": 1.8432237261257556,
        "ILE": 1.7070782006170608,
        "LEU": 1.6985800823090673,
        "LYS": 2.0501078864146676,
        "MET": 1.772408399874025,
        "NME": 0.0,
        "PHE": 2.0497878966957535,
        "PRO": 1.354330791914399,
        "SER": 1.0133719879708,
        "THR": 1.3046137047129012,
        "TRP": 2.480105037382033,
        "TYR": 2.195561598795418,
        "VAL": 1.4346159343072447,
}

# (residue, atom): (amber_type, crippen_type, surf)
ATOM_DATA = {
    ("ACE", "C"): ("C", "C1", float("nan")),
    ("ACE", "CH3"): ("CT", "C1", float("nan")),
    ("ACE", "H1"): ("HC", "H1", float("nan")),
    ("ACE", "H2"): ("HC", "H1", float("nan")),
    ("ACE", "H3"): ("HC", "H1", float("nan")),
    ("ACE", "HH31"): ("HC", "H1", float("nan")),
    ("ACE", "HH32"): ("HC", "H1", float("nan")),
    ("ACE", "HH33"): ("HC", "H1", float("nan")),
    ("ACE", "O"): ("O", "O9", float("nan")),
    ("ALA", "C"): ("C", "C5", 0.0222620835833285),
    ("ALA", "CA"): ("CX", "C4", 0.0007040712127453),
    ("ALA", "CB"): ("CT", "C1", 0.0744767934949999),
    ("ALA", "H"): ("H", "H3", 0.112012150725),
    ("ALA", "HA"): ("H1", "H1", 0.127920454921),
    ("ALA", "HB1"): ("HC", "H1", 0.2146160372499998),
    ("ALA", "HB2"): ("HC", "H1", 0.2158533003299998),
    ("ALA", "HB3"): ("HC", "H1", 0.2146929514899998),
    ("ALA", "N"): ("N", "N2", 0.0140719738646999),
    ("ALA", "O"): ("O", "O9", 0.3190807342899996),
    ("ARG", "C"): ("C", "C5", 0.017854971796336),
    ("ARG", "CA"): ("CX", "C4", 0.0003803782077974),
    ("ARG", "CB"): ("C8", "C1", 0.0067094922837352),
    ("ARG", "CD"): ("C8", "C3", 0.0159543479818481),
    ("ARG", "CG"): ("C8", "C1", 0.0091378370642604),
    ("ARG", "CZ"): ("CA", "C5", 0.08507683805),
    ("ARG", "H"): ("H", "H3", 0.0892037992269999),
    ("ARG", "HA"): ("H1", "H1", 0.0832653822984289),
    ("ARG", "HB2"): ("HC", "H1", 0.1291611695562999),
    ("ARG", "HB3"): ("HC", "H1", 0.1170286511663999),
    ("ARG", "HD2"): ("H1", "H1", 0.1528517121104001),
    ("ARG", "HD3"): ("H1", "H1", 0.1529013251257898),
    ("ARG", "HE"): ("H", "H3", 0.1319919950789002),
    ("ARG", "HG2"): ("HC", "H1", 0.1301399460017001),
    ("ARG", "HG3"): ("HC", "H1", 0.1257868380481698),
    ("ARG", "HH11"): ("H", "H3", 0.1651677266786899),
    ("ARG", "HH12"): ("H", "H3", 0.2472029511499997),
    ("ARG", "HH21"): ("H", "H3", 0.2487688408699998),
    ("ARG", "HH22"): ("H", "H3", 0.2484871981800002),
    ("ARG", "N"): ("N", "N2", 0.0073353567401762),
    ("ARG", "NE"): ("N2", "N2", 0.0310931109111),
    ("ARG", "NH1"): ("N2", "N10", 0.1218840198919999),
    ("ARG", "NH2"): ("N2", "N1", 0.1376894548769998),
    ("ARG", "O"): ("O", "O9", 0.2991225484399998),
    ("ASN", "C"): ("C", "C5", 0.017825978819874),
    ("ASN", "CA"): ("CX", "C4", 0.0003627432063012),
    ("ASN", "CB"): ("2C", "C1", 0.0137955635853471),
    ("ASN", "CG"): ("C", "C5", 0.047104849955),
    ("ASN", "H"): ("H", "H3", 0.0886935977131),
    ("ASN", "HA"): ("H1", "H1", 0.083979212451),
    ("ASN", "HB2"): ("HC", "H1", 0.1571243953030002),
    ("ASN", "HB3"): ("HC", "H1", 0.150888226305),
    ("ASN", "HD21"): ("H", "H3", 0.28301205732),
    ("ASN", "HD22"): ("H", "H3", 0.2174562430879998),
    ("ASN", "N"): ("N", "N2", 0.0080777818238652),
    ("ASN", "ND2"): ("N", "N1", 0.116470234276),
    ("ASN", "O"): ("O", "O9", 0.3020501998600003),
    ("ASN", "OD1"): ("O", "O9", 0.3537631195099996),
    ("ASP", "C"): ("C", "C5", 0.018643469681618),
    ("ASP", "CA"): ("CX", "C4", 0.0003073127743756),
    ("ASP", "CB"): ("2C", "C1", 0.0127665224059839),
    ("ASP", "CG"): ("CO", "C5", 0.0509728429969999),
    ("ASP", "H"): ("H", "H3", 0.0813665036224001),
    ("ASP", "HA"): ("H1", "H1", 0.094912805299),
    ("ASP", "HB2"): ("HC", "H1", 0.1644520883599997),
    ("ASP", "HB3"): ("HC", "H1", 0.1713895980760001),
    ("ASP", "N"): ("N", "N2", 0.0064229689714204),
    ("ASP", "O"): ("O", "O9", 0.3108739100899997),
    ("ASP", "OD1"): ("O2", "O9", 0.4196967243099995),
    ("ASP", "OD2"): ("O2", "O12", 0.4120946376099995),
    ("CYS", "C"): ("C", "C5", 0.0166736067290699),
    ("CYS", "CA"): ("CX", "C4", 0.0004269792667541),
    ("CYS", "CB"): ("2C", "C3", 0.0201535849503509),
    ("CYS", "H"): ("H", "H3", 0.0876131688575),
    ("CYS", "HA"): ("H1", "H1", 0.1021574149709999),
    ("CYS", "HB2"): ("H1", "H1", 0.1827259923969998),
    ("CYS", "HB3"): ("H1", "H1", 0.1797528269370001),
    ("CYS", "HG"): ("HS", "H2", 0.2129820465379998),
    ("CYS", "N"): ("N", "N2", 0.0090859639541411),
    ("CYS", "O"): ("O", "O9", 0.3052087796199999),
    ("CYS", "SG"): ("SH", "S1", 0.4886940372699994),
    ("CYX", "C"): ("C", "C5", 0.0166736067290699),
    ("CYX", "CA"): ("CX", "C4", 0.0004269792667541),
    ("CYX", "CB"): ("2C", "C3", 0.0201535849503509),
    ("CYX", "H"): ("H", "H3", 0.0876131688575),
    ("CYX", "HA"): ("H1", "H1", 0.1021574149709999),
    ("CYX", "HB2"): ("H1", "H1", 0.1827259923969998),
    ("CYX", "HB3"): ("H1", "H1", 0.1797528269370001),
    ("CYX", "N"): ("N", "N2", 0.0090859639541411),
    ("CYX", "O"): ("O", "O9", 0.3052087796199999),
    ("CYX", "SG"): ("S", "S1", 0.4886940372699994),
    ("GLN", "C"): ("C", "C5", 0.0192102424636515),
    ("GLN", "CA"): ("CX", "C4", 0.0004194205007441),
    ("GLN", "CB"): ("2C", "C1", 0.0088556974917505),
    ("GLN", "CD"): ("C", "C5", 0.0536995476409999),
    ("GLN", "CG"): ("2C", "C1", 0.0124629897422783),
    ("GLN", "H"): ("H", "H3", 0.0824824601454843),
    ("GLN", "HA"): ("H1", "H1", 0.0794791762033999),
    ("GLN", "HB2"): ("HC", "H1", 0.1459339428219999),
    ("GLN", "HB3"): ("HC", "H1", 0.1363643583389999),
    ("GLN", "HE21"): ("H", "H3", 0.2802045140299996),
    ("GLN", "HE22"): ("H", "H3", 0.2276661129830001),
    ("GLN", "HG2"): ("HC", "H1", 0.1359080961338998),
    ("GLN", "HG3"): ("HC", "H1", 0.1547294299209999),
    ("GLN", "N"): ("N", "N2", 0.00668645409244),
    ("GLN", "NE2"): ("N", "N1", 0.1249608960420001),
    ("GLN", "O"): ("O", "O9", 0.29791808525),
    ("GLN", "OE1"): ("O", "O9", 0.3541216339699998),
    ("GLU", "C"): ("C", "C5", 0.0180137075894485),
    ("GLU", "CA"): ("CX", "C4", 0.0004118585540853),
    ("GLU", "CB"): ("2C", "C1", 0.0107550346314765),
    ("GLU", "CD"): ("CO", "C5", 0.0490974099229999),
    ("GLU", "CG"): ("2C", "C1", 0.01861319333547),
    ("GLU", "H"): ("H", "H3", 0.0788299783053004),
    ("GLU", "HA"): ("H1", "H1", 0.0783552853657999),
    ("GLU", "HB2"): ("HC", "H1", 0.154184661641),
    ("GLU", "HB3"): ("HC", "H1", 0.14949430067),
    ("GLU", "HG2"): ("HC", "H1", 0.1629262626119998),
    ("GLU", "HG3"): ("HC", "H1", 0.1807004524329999),
    ("GLU", "N"): ("N", "N2", 0.0076421089306325),
    ("GLU", "O"): ("O", "O9", 0.3017808477800001),
    ("GLU", "OE1"): ("O2", "O9", 0.4037761238399999),
    ("GLU", "OE2"): ("O2", "O12", 0.3948835985900001),
    ("GLY", "C"): ("C", "C5", 0.050698146564),
    ("GLY", "CA"): ("CX", "C3", 0.0252622044201999),
    ("GLY", "H"): ("H", "H3", 0.1677513115879998),
    ("GLY", "HA2"): ("H1", "H1", 0.194410640527),
    ("GLY", "HA3"): ("H1", "H1", 0.1923610688329999),
    ("GLY", "N"): ("N", "N2", 0.0306311932409),
    ("GLY", "O"): ("O", "O9", 0.3365100703000003),
    ("HID", "C"): ("C", "C5", 0.0159517910914147),
    ("HID", "CA"): ("CX", "C4", 0.000525217898625),
    ("HID", "CB"): ("CT", "C10", 0.0165614213422709),
    ("HID", "CD2"): ("CV", "C18", 0.1181619689920001),
    ("HID", "CE1"): ("CR", "C18", 0.1814969931649997),
    ("HID", "CG"): ("CC", "C21", 0.0340461420457999),
    ("HID", "H"): ("H", "H3", 0.084337039458423),
    ("HID", "HA"): ("H1", "H1", 0.085052561441),
    ("HID", "HB2"): ("HC", "H1", 0.1611272674410002),
    ("HID", "HB3"): ("HC", "H1", 0.1523975751220001),
    ("HID", "HD1"): ("H", "H3", 0.199610225663),
    ("HID", "HD2"): ("H4", "H1", 0.205079287509),
    ("HID", "HE1"): ("H5", "H1", 0.29029394236),
    ("HID", "N"): ("N", "N2", 0.0101613860184109),
    ("HID", "ND1"): ("NA", "N11", 0.0376655273604999),
    ("HID", "NE2"): ("NB", "N11", 0.2846645096699997),
    ("HID", "O"): ("O", "O9", 0.2857659955800005),
    ("HIE", "C"): ("C", "C5", 0.0156003536441001),
    ("HIE", "CA"): ("CX", "C4", 0.000721704654803),
    ("HIE", "CB"): ("CT", "C10", 0.0164657191481759),
    ("HIE", "CD2"): ("CW", "C18", 0.1102698660610002),
    ("HIE", "CE1"): ("CR", "C18", 0.1785786781419998),
    ("HIE", "CG"): ("CC", "C21", 0.0315875289046),
    ("HIE", "H"): ("H", "H3", 0.0911884935746999),
    ("HIE", "HA"): ("H1", "H1", 0.0894287734335),
    ("HIE", "HB2"): ("HC", "H1", 0.1700504923710001),
    ("HIE", "HB3"): ("HC", "H1", 0.1530483707699998),
    ("HIE", "HD2"): ("H4", "H1", 0.2001506357609996),
    ("HIE", "HE1"): ("H5", "H1", 0.2900619128700002),
    ("HIE", "HE2"): ("H", "H3", 0.3051465024899995),
    ("HIE", "N"): ("N", "N2", 0.0112368456369072),
    ("HIE", "ND1"): ("NB", "N11", 0.177384917609),
    ("HIE", "NE2"): ("NA", "N11", 0.060564509361),
    ("HIE", "O"): ("O", "O9", 0.2877492927000001),
    ("HIP", "C"): ("C", "C5", 0.0199066346814043),
    ("HIP", "CA"): ("CX", "C4", 0.0004446095222605),
    ("HIP", "CB"): ("CT", "C10", 0.0143182529045566),
    ("HIP", "CD2"): ("CW", "C18", 0.1175977421319999),
    ("HIP", "CE1"): ("CR", "C18", 0.1831192939039998),
    ("HIP", "CG"): ("CC", "C21", 0.0287963759122),
    ("HIP", "H"): ("H", "H3", 0.094360039274),
    ("HIP", "HA"): ("H1", "H1", 0.085368078618),
    ("HIP", "HB2"): ("HC", "H1", 0.1542511000580001),
    ("HIP", "HB3"): ("HC", "H1", 0.152002423285),
    ("HIP", "HD1"): ("H", "H3", 0.1980053423930001),
    ("HIP", "HD2"): ("H4", "H1", 0.211678285802),
    ("HIP", "HE1"): ("H5", "H1", 0.2873358386599994),
    ("HIP", "HE2"): ("H", "H3", 0.30704445842),
    ("HIP", "N"): ("N", "N2", 0.0079649068073041),
    ("HIP", "ND1"): ("NA", "N11", 0.039238189874),
    ("HIP", "NE2"): ("NA", "N12", 0.0644683441629999),
    ("HIP", "O"): ("O", "O9", 0.2790977380200001),
    ("ILE", "C"): ("C", "C5", 0.0092209359931301),
    ("ILE", "CA"): ("CX", "C4", 0.0001612199084989),
    ("ILE", "CB"): ("3C", "C2", 8.815129329701602e-06),
    ("ILE", "CD1"): ("CT", "C1", 0.080609271737),
    ("ILE", "CG1"): ("2C", "C1", 0.0114893171625315),
    ("ILE", "CG2"): ("CT", "C1", 0.0647707735220001),
    ("ILE", "H"): ("H", "H3", 0.0702231720208069),
    ("ILE", "HA"): ("H1", "H1", 0.0598636906451999),
    ("ILE", "HB"): ("HC", "H1", 0.1103896160269998),
    ("ILE", "HD11"): ("HC", "H1", 0.2092613557649998),
    ("ILE", "HD12"): ("HC", "H1", 0.2054104417310003),
    ("ILE", "HD13"): ("HC", "H1", 0.2080037128120002),
    ("ILE", "HG12"): ("HC", "H1", 0.1425400641119999),
    ("ILE", "HG13"): ("HC", "H1", 0.1363722022709999),
    ("ILE", "HG21"): ("HC", "H1", 0.1598053322280001),
    ("ILE", "HG22"): ("HC", "H1", 0.1598086474019997),
    ("ILE", "HG23"): ("HC", "H1", 0.1587449600730001),
    ("ILE", "N"): ("N", "N2", 0.0041934399966883),
    ("ILE", "O"): ("O", "O9", 0.2806116957099999),
    ("LEU", "C"): ("C", "C5", 0.0187819513448897),
    ("LEU", "CA"): ("CX", "C4", 0.0001801128669122),
    ("LEU", "CB"): ("2C", "C1", 0.003724398542533),
    ("LEU", "CD1"): ("CT", "C1", 0.0724892463859999),
    ("LEU", "CD2"): ("CT", "C1", 0.0715055213629999),
    ("LEU", "CG"): ("3C", "C2", 8.564807403462929e-05),
    ("LEU", "H"): ("H", "H3", 0.088574940777),
    ("LEU", "HA"): ("H1", "H1", 0.0516393113845001),
    ("LEU", "HB2"): ("HC", "H1", 0.122137090769),
    ("LEU", "HB3"): ("HC", "H1", 0.1040944271669999),
    ("LEU", "HD11"): ("HC", "H1", 0.1986696285509998),
    ("LEU", "HD12"): ("HC", "H1", 0.2003967639280001),
    ("LEU", "HD13"): ("HC", "H1", 0.2011700499879999),
    ("LEU", "HD21"): ("HC", "H1", 0.1888724243149999),
    ("LEU", "HD22"): ("HC", "H1", 0.188001734958),
    ("LEU", "HD23"): ("HC", "H1", 0.1885261095499999),
    ("LEU", "HG"): ("HC", "H1", 0.1072677273330001),
    ("LEU", "N"): ("N", "N2", 0.0048229484569497),
    ("LEU", "O"): ("O", "O9", 0.30596434115),
    ("LYS", "C"): ("C", "C5", 0.0170804002987168),
    ("LYS", "CA"): ("CX", "C4", 0.0003854115907405),
    ("LYS", "CB"): ("C8", "C1", 0.0061993412000689),
    ("LYS", "CD"): ("C8", "C1", 0.0100837206989994),
    ("LYS", "CE"): ("C8", "C3", 0.0171760532079309),
    ("LYS", "CG"): ("C8", "C1", 0.006468883838159),
    ("LYS", "H"): ("H", "H3", 0.0939500292489999),
    ("LYS", "HA"): ("H1", "H1", 0.0856195693933),
    ("LYS", "HB2"): ("HC", "H1", 0.1332796168310001),
    ("LYS", "HB3"): ("HC", "H1", 0.1216340922099999),
    ("LYS", "HD2"): ("HC", "H1", 0.1587901985365099),
    ("LYS", "HD3"): ("HC", "H1", 0.1574403482511999),
    ("LYS", "HE2"): ("HP", "H1", 0.1933008785740001),
    ("LYS", "HE3"): ("HP", "H1", 0.192908458339),
    ("LYS", "HG2"): ("HC", "H1", 0.1123565730463999),
    ("LYS", "HG3"): ("HC", "H1", 0.1108820009540999),
    ("LYS", "HZ1"): ("H", "H3", 0.244258147307),
    ("LYS", "HZ2"): ("H", "H3", 0.2424764116149999),
    ("LYS", "HZ3"): ("H", "H3", 0.242527572921),
    ("LYS", "N"): ("N", "N2", 0.0079910788098054),
    ("LYS", "NZ"): ("N3", "N10", 0.0147060194909999),
    ("LYS", "O"): ("O", "O9", 0.29922664261),
    ("MET", "C"): ("C", "C5", 0.0183423736745599),
    ("MET", "CA"): ("CX", "C4", 0.0005126241786315),
    ("MET", "CB"): ("2C", "C1", 0.0081024427884584),
    ("MET", "CE"): ("CT", "C3", 0.094727259462),
    ("MET", "CG"): ("2C", "C3", 0.0157717099698064),
    ("MET", "H"): ("H", "H3", 0.0933857546379798),
    ("MET", "HA"): ("H1", "H1", 0.0889975278493599),
    ("MET", "HB2"): ("HC", "H1", 0.125716809927),
    ("MET", "HB3"): ("HC", "H1", 0.1271801203746998),
    ("MET", "HE1"): ("H1", "H1", 0.2163952787876998),
    ("MET", "HE2"): ("H1", "H1", 0.2185996956710003),
    ("MET", "HE3"): ("H1", "H1", 0.2212761345829999),
    ("MET", "HG2"): ("H1", "H1", 0.13835962737),
    ("MET", "HG3"): ("H1", "H1", 0.130679280061),
    ("MET", "N"): ("N", "N2", 0.0092467471669174),
    ("MET", "O"): ("O", "O9", 0.2911258339299999),
    ("MET", "SD"): ("S", "S1", 0.3866025130300004),
    ("NME", "CH3"): ("CT", "C3", float("nan")),
    ("NME", "H"): ("H", "H3", float("nan")),
    ("NME", "HH31"): ("H1", "H1", float("nan")),
    ("NME", "HH32"): ("H1", "H1", float("nan")),
    ("NME", "HH33"): ("H1", "H1", float("nan")),
    ("NME", "N"): ("N", "N2", float("nan")),
    ("PHE", "C"): ("C", "C5", 0.0169909908955751),
    ("PHE", "CA"): ("CX", "C4", 0.0005302591839483),
    ("PHE", "CB"): ("CT", "C10", 0.0150273574963535),
    ("PHE", "CD1"): ("CA", "C18", 0.0742260979059998),
    ("PHE", "CD2"): ("CA", "C18", 0.074778949198),
    ("PHE", "CE1"): ("CA", "C18", 0.1229468845749999),
    ("PHE", "CE2"): ("CA", "C18", 0.123523730704),
    ("PHE", "CG"): ("CA", "C21", 0.0248667245845999),
    ("PHE", "CZ"): ("CA", "C18", 0.1333290948570001),
    ("PHE", "H"): ("H", "H3", 0.0899449679992),
    ("PHE", "HA"): ("H1", "H1", 0.0696200580818),
    ("PHE", "HB2"): ("HC", "H1", 0.14817723161),
    ("PHE", "HB3"): ("HC", "H1", 0.137664543155),
    ("PHE", "HD1"): ("HA", "H1", 0.1633780196039999),
    ("PHE", "HD2"): ("HA", "H1", 0.164364370654),
    ("PHE", "HE1"): ("HA", "H1", 0.2649808880000003),
    ("PHE", "HE2"): ("HA", "H1", 0.2653767877999999),
    ("PHE", "HZ"): ("HA", "H1", 0.2675271584700001),
    ("PHE", "N"): ("N", "N2", 0.0096561245950722),
    ("PHE", "O"): ("O", "O9", 0.28938617596),
    ("PRO", "C"): ("C", "C5", 0.0089702845550326),
    ("PRO", "CA"): ("CX", "C4", 0.0002808705547725),
    ("PRO", "CB"): ("CT", "C1", 0.0292712299523),
    ("PRO", "CD"): ("CT", "C3", 0.0196447457301),
    ("PRO", "CG"): ("CT", "C1", 0.040785820223),
    ("PRO", "HA"): ("H1", "H1", 0.126959471712),
    ("PRO", "HB2"): ("HC", "H1", 0.1711574880449997),
    ("PRO", "HB3"): ("HC", "H1", 0.2135009799199998),
    ("PRO", "HD2"): ("H1", "H1", 0.1589849709559999),
    ("PRO", "HD3"): ("H1", "H1", 0.1607881964559999),
    ("PRO", "HG2"): ("HC", "H1", 0.2027747791499998),
    ("PRO", "HG3"): ("HC", "H1", 0.2304631097699999),
    ("PRO", "N"): ("N", "N7", 0.0031966624648994),
    ("PRO", "O"): ("O", "O9", 0.2798629660100001),
    ("SER", "C"): ("C", "C5", 0.021272135269939),
    ("SER", "CA"): ("CX", "C4", 0.0007267459507842),
    ("SER", "CB"): ("2C", "C3", 0.0269437110733),
    ("SER", "H"): ("H", "H3", 0.106065745678),
    ("SER", "HA"): ("H1", "H1", 0.120966230682),
    ("SER", "HB2"): ("H1", "H1", 0.185107522014),
    ("SER", "HB3"): ("H1", "H1", 0.1887051055970002),
    ("SER", "HG"): ("HO", "H2", 0.2265005966444999),
    ("SER", "N"): ("N", "N2", 0.0117089182026779),
    ("SER", "O"): ("O", "O9", 0.3059932114699995),
    ("SER", "OG"): ("OH", "O2", 0.2651488219599999),
    ("THR", "C"): ("C", "C5", 0.016994714146562),
    ("THR", "CA"): ("CX", "C4", 0.0003917139952643),
    ("THR", "CB"): ("3C", "C4", 0.0004912153249012),
    ("THR", "CG2"): ("CT", "C1", 0.072961582885),
    ("THR", "H"): ("H", "H3", 0.071831542066),
    ("THR", "HA"): ("H1", "H1", 0.0865592087340001),
    ("THR", "HB"): ("H1", "H1", 0.1429987999769998),
    ("THR", "HG1"): ("HO", "H2", 0.1855804690289998),
    ("THR", "HG21"): ("HC", "H1", 0.1995589472560002),
    ("THR", "HG22"): ("HC", "H1", 0.198653699566),
    ("THR", "HG23"): ("HC", "H1", 0.198387064811),
    ("THR", "N"): ("N", "N2", 0.0054741489488986),
    ("THR", "O"): ("O", "O9", 0.2944578196199994),
    ("THR", "OG1"): ("OH", "O2", 0.2194227171300001),
    ("TRP", "C"): ("C", "C5", 0.0157352502466327),
    ("TRP", "CA"): ("CX", "C4", 0.0005302607717932),
    ("TRP", "CB"): ("CT", "C10", 0.0147930674082226),
    ("TRP", "CD1"): ("CW", "C18", 0.1074258380450001),
    ("TRP", "CD2"): ("CB", "C19", 0.0316606069054999),
    ("TRP", "CE2"): ("CN", "C19", 0.0577930851289999),
    ("TRP", "CE3"): ("CA", "C18", 0.0781558598629999),
    ("TRP", "CG"): ("C*", "C21", 0.0266590380529),
    ("TRP", "CH2"): ("CA", "C18", 0.135767575909),
    ("TRP", "CZ2"): ("CA", "C18", 0.1335759470959999),
    ("TRP", "CZ3"): ("CA", "C18", 0.118329413559),
    ("TRP", "H"): ("H", "H3", 0.0940243852309709),
    ("TRP", "HA"): ("H1", "H1", 0.067041019377412),
    ("TRP", "HB2"): ("HC", "H1", 0.1463845994169998),
    ("TRP", "HB3"): ("HC", "H1", 0.1308272103259999),
    ("TRP", "HD1"): ("H4", "H1", 0.2050596303789999),
    ("TRP", "HE1"): ("H", "H3", 0.2693400882399997),
    ("TRP", "HE3"): ("HA", "H1", 0.1231423818129999),
    ("TRP", "HH2"): ("HA", "H1", 0.2678725646799997),
    ("TRP", "HZ2"): ("HA", "H1", 0.2432494320300001),
    ("TRP", "HZ3"): ("HA", "H1", 0.2617367044800001),
    ("TRP", "N"): ("N", "N2", 0.0115664251840116),
    ("TRP", "NE1"): ("NA", "N11", 0.0612909746719998),
    ("TRP", "O"): ("O", "O9", 0.2773914874099997),
    ("TYR", "C"): ("C", "C5", 0.017402775064742),
    ("TYR", "CA"): ("CX", "C4", 0.000454690516484),
    ("TYR", "CB"): ("CT", "C10", 0.0145626193381177),
    ("TYR", "CD1"): ("CA", "C18", 0.0773170284080001),
    ("TYR", "CD2"): ("CA", "C18", 0.074965472409),
    ("TYR", "CE1"): ("CA", "C18", 0.119532306615),
    ("TYR", "CE2"): ("CA", "C18", 0.11457740211),
    ("TYR", "CG"): ("CA", "C21", 0.0250040117571),
    ("TYR", "CZ"): ("C", "C23", 0.0679649858749999),
    ("TYR", "H"): ("H", "H3", 0.0811699650433199),
    ("TYR", "HA"): ("H1", "H1", 0.0675192452791999),
    ("TYR", "HB2"): ("HC", "H1", 0.143189171899),
    ("TYR", "HB3"): ("HC", "H1", 0.1402799033589999),
    ("TYR", "HD1"): ("HA", "H1", 0.1668957069299998),
    ("TYR", "HD2"): ("HA", "H1", 0.160825317446),
    ("TYR", "HE1"): ("HA", "H1", 0.2324301465500001),
    ("TYR", "HE2"): ("HA", "H1", 0.2309352101300001),
    ("TYR", "HH"): ("HO", "H2", 0.2375448511299999),
    ("TYR", "N"): ("N", "N2", 0.0084632604179598),
    ("TYR", "O"): ("O", "O9", 0.2955584097299997),
    ("TYR", "OH"): ("OH", "O2", 0.3220182195600003),
    ("VAL", "C"): ("C", "C5", 0.0125913620399483),
    ("VAL", "CA"): ("CX", "C4", 0.0002607212342882),
    ("VAL", "CB"): ("3C", "C2", 3.400732424491059e-05),
    ("VAL", "CG1"): ("CT", "C1", 0.068596059517),
    ("VAL", "CG2"): ("CT", "C1", 0.0702435348289999),
    ("VAL", "H"): ("H", "H3", 0.0665937443058999),
    ("VAL", "HA"): ("H1", "H1", 0.076037557227),
    ("VAL", "HB"): ("HC", "H1", 0.1424789239360001),
    ("VAL", "HG11"): ("HC", "H1", 0.1764655893790002),
    ("VAL", "HG12"): ("HC", "H1", 0.1760559587759998),
    ("VAL", "HG13"): ("HC", "H1", 0.1791628860549999),
    ("VAL", "HG21"): ("HC", "H1", 0.1831723235450001),
    ("VAL", "HG22"): ("HC", "H1", 0.1818121165449999),
    ("VAL", "HG23"): ("HC", "H1", 0.1805569771739998),
    ("VAL", "N"): ("N", "N2", 0.0056452274000979),
    ("VAL", "O"): ("O", "O9", 0.2844149681799998),
}
