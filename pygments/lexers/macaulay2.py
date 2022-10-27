"""
    pygments.lexers.macaulay2
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexer for Macaulay2.

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, words
from pygments.token import Comment, Keyword, Name, String, Text

__all__ = ['Macaulay2Lexer']

# Auto-generated for Macaulay2-1.20. Do not modify this file manually.

M2KEYWORDS = (
    "and",
    "break",
    "catch",
    "continue",
    "do",
    "elapsedTime",
    "elapsedTiming",
    "else",
    "for",
    "from",
    "global",
    "if",
    "in",
    "list",
    "local",
    "new",
    "not",
    "of",
    "or",
    "return",
    "shield",
    "SPACE",
    "step",
    "symbol",
    "then",
    "threadVariable",
    "throw",
    "time",
    "timing",
    "to",
    "try",
    "when",
    "while",
    "xor"
    )

M2DATATYPES = (
    "Adjacent",
    "AffineVariety",
    "Analyzer",
    "ANCHOR",
    "AngleBarList",
    "Array",
    "AssociativeExpression",
    "Bag",
    "BasicList",
    "BettiTally",
    "BinaryOperation",
    "BLOCKQUOTE",
    "BODY",
    "BOLD",
    "Boolean",
    "BR",
    "CacheFunction",
    "CacheTable",
    "CC",
    "CDATA",
    "ChainComplex",
    "ChainComplexMap",
    "CODE",
    "CoherentSheaf",
    "Command",
    "COMMENT",
    "CompiledFunction",
    "CompiledFunctionBody",
    "CompiledFunctionClosure",
    "ComplexField",
    "Constant",
    "Database",
    "DD",
    "Descent",
    "Describe",
    "Dictionary",
    "DIV",
    "Divide",
    "DL",
    "DocumentTag",
    "DT",
    "Eliminate",
    "EM",
    "EngineRing",
    "Equation",
    "ExampleItem",
    "Expression",
    "File",
    "FilePosition",
    "FractionField",
    "Function",
    "FunctionApplication",
    "FunctionBody",
    "FunctionClosure",
    "GaloisField",
    "GeneralOrderedMonoid",
    "GlobalDictionary",
    "GradedModule",
    "GradedModuleMap",
    "GroebnerBasis",
    "GroebnerBasisOptions",
    "HashTable",
    "HEAD",
    "HEADER1",
    "HEADER2",
    "HEADER3",
    "HEADER4",
    "HEADER5",
    "HEADER6",
    "HeaderType",
    "Holder",
    "HR",
    "HREF",
    "HTML",
    "Hybrid",
    "Hypertext",
    "HypertextContainer",
    "HypertextParagraph",
    "Ideal",
    "IMG",
    "ImmutableType",
    "IndeterminateNumber",
    "IndexedVariable",
    "IndexedVariableTable",
    "InexactField",
    "InexactFieldFamily",
    "InexactNumber",
    "InfiniteNumber",
    "IntermediateMarkUpType",
    "ITALIC",
    "Keyword",
    "LABEL",
    "LATER",
    "LI",
    "LINK",
    "List",
    "LITERAL",
    "LocalDictionary",
    "LowerBound",
    "Manipulator",
    "MapExpression",
    "MarkUpType",
    "Matrix",
    "MatrixExpression",
    "MENU",
    "META",
    "MethodFunction",
    "MethodFunctionBinary",
    "MethodFunctionSingle",
    "MethodFunctionWithOptions",
    "Minus",
    "Module",
    "Monoid",
    "MonoidElement",
    "MonomialIdeal",
    "MultigradedBettiTally",
    "MutableHashTable",
    "MutableList",
    "MutableMatrix",
    "Net",
    "NetFile",
    "NonAssociativeProduct",
    "Nothing",
    "Number",
    "NumberedVerticalList",
    "OL",
    "OneExpression",
    "Option",
    "OptionTable",
    "OrderedMonoid",
    "Package",
    "PARA",
    "Parenthesize",
    "Parser",
    "Partition",
    "PolynomialRing",
    "Power",
    "PRE",
    "Product",
    "ProductOrder",
    "Program",
    "ProgramRun",
    "ProjectiveHilbertPolynomial",
    "ProjectiveVariety",
    "Pseudocode",
    "QQ",
    "QuotientRing",
    "RealField",
    "Resolution",
    "Ring",
    "RingElement",
    "RingFamily",
    "RingMap",
    "RowExpression",
    "RR",
    "RRi",
    "SCRIPT",
    "ScriptedFunctor",
    "SelfInitializingType",
    "Sequence",
    "Set",
    "SheafExpression",
    "SheafOfRings",
    "SMALL",
    "SPAN",
    "SparseMonomialVectorExpression",
    "SparseVectorExpression",
    "String",
    "STRONG",
    "STYLE",
    "SUB",
    "Subscript",
    "SUBSECTION",
    "Sum",
    "SumOfTwists",
    "SUP",
    "Superscript",
    "Symbol",
    "SymbolBody",
    "TABLE",
    "Table",
    "Tally",
    "Task",
    "TD",
    "TestInput",
    "TEX",
    "TH",
    "Thing",
    "Time",
    "TITLE",
    "TO",
    "TO2",
    "TOH",
    "TR",
    "TT",
    "Type",
    "UL",
    "URL",
    "Variety",
    "Vector",
    "VectorExpression",
    "VerticalList",
    "VirtualTally",
    "VisibleList",
    "WrapperType",
    "ZeroExpression",
    "ZZ"
    )

M2FUNCTIONS = (
    "about",
    "abs",
    "accumulate",
    "acos",
    "acosh",
    "acot",
    "acoth",
    "addCancelTask",
    "addDependencyTask",
    "addEndFunction",
    "addHook",
    "addStartFunction",
    "addStartTask",
    "adjoint",
    "agm",
    "alarm",
    "all",
    "ambient",
    "analyticSpread",
    "ancestor",
    "ancestors",
    "andP",
    "ann",
    "annihilator",
    "antipode",
    "any",
    "append",
    "applicationDirectory",
    "apply",
    "applyKeys",
    "applyPairs",
    "applyTable",
    "applyValues",
    "apropos",
    "arXiv",
    "ascii",
    "asin",
    "asinh",
    "ass",
    "assert",
    "associatedGradedRing",
    "associatedPrimes",
    "atan",
    "atan2",
    "atanh",
    "atEndOfFile",
    "autoload",
    "baseFilename",
    "baseName",
    "baseRing",
    "basis",
    "beginDocumentation",
    "benchmark",
    "BesselJ",
    "BesselY",
    "Beta",
    "betti",
    "between",
    "binomial",
    "borel",
    "cacheValue",
    "cancelTask",
    "capture",
    "ceiling",
    "centerString",
    "chainComplex",
    "char",
    "characters",
    "charAnalyzer",
    "check",
    "checkDegrees",
    "chi",
    "class",
    "clean",
    "clearEcho",
    "code",
    "codim",
    "coefficient",
    "coefficientRing",
    "coefficients",
    "cohomology",
    "coimage",
    "coker",
    "cokernel",
    "collectGarbage",
    "columnAdd",
    "columnate",
    "columnMult",
    "columnPermute",
    "columnRankProfile",
    "columnSwap",
    "combine",
    "commandInterpreter",
    "commonest",
    "commonRing",
    "comodule",
    "complement",
    "complete",
    "components",
    "compose",
    "compositions",
    "compress",
    "concatenate",
    "conductor",
    "cone",
    "conjugate",
    "connectionCount",
    "constParser",
    "content",
    "contract",
    "conwayPolynomial",
    "copy",
    "copyDirectory",
    "copyFile",
    "cos",
    "cosh",
    "cot",
    "cotangentSheaf",
    "coth",
    "cover",
    "coverMap",
    "cpuTime",
    "createTask",
    "csc",
    "csch",
    "currentColumnNumber",
    "currentDirectory",
    "currentPosition",
    "currentRowNumber",
    "currentTime",
    "deadParser",
    "debug",
    "debugError",
    "decompose",
    "deepSplice",
    "default",
    "degree",
    "degreeLength",
    "degrees",
    "degreesMonoid",
    "degreesRing",
    "delete",
    "demark",
    "denominator",
    "depth",
    "describe",
    "det",
    "determinant",
    "diagonalMatrix",
    "diameter",
    "dictionary",
    "diff",
    "difference",
    "Digamma",
    "dim",
    "directSum",
    "disassemble",
    "discriminant",
    "dismiss",
    "distinguished",
    "divideByVariable",
    "doc",
    "document",
    "drop",
    "dual",
    "eagonNorthcott",
    "echoOff",
    "echoOn",
    "eigenvalues",
    "eigenvectors",
    "eint",
    "elements",
    "eliminate",
    "End",
    "endPackage",
    "entries",
    "erase",
    "erf",
    "erfc",
    "error",
    "euler",
    "eulers",
    "even",
    "EXAMPLE",
    "examples",
    "exec",
    "exp",
    "expectedReesIdeal",
    "expm1",
    "exponents",
    "export",
    "exportFrom",
    "exportMutable",
    "expression",
    "extend",
    "exteriorPower",
    "factor",
    "Fano",
    "fileExecutable",
    "fileExists",
    "fileLength",
    "fileMode",
    "fileReadable",
    "fileTime",
    "fileWritable",
    "fillMatrix",
    "findFiles",
    "findHeft",
    "findProgram",
    "findSynonyms",
    "first",
    "firstkey",
    "fittingIdeal",
    "flagLookup",
    "flatten",
    "flattenRing",
    "flip",
    "floor",
    "fold",
    "forceGB",
    "fork",
    "format",
    "formation",
    "frac",
    "fraction",
    "frames",
    "fromDividedPowers",
    "fromDual",
    "functionBody",
    "futureParser",
    "Gamma",
    "gb",
    "gbRemove",
    "gbSnapshot",
    "gcd",
    "gcdCoefficients",
    "gcdLLL",
    "GCstats",
    "genera",
    "generateAssertions",
    "generator",
    "generators",
    "genericMatrix",
    "genericSkewMatrix",
    "genericSymmetricMatrix",
    "gens",
    "genus",
    "get",
    "getc",
    "getChangeMatrix",
    "getenv",
    "getGlobalSymbol",
    "getNetFile",
    "getNonUnit",
    "getPrimeWithRootOfUnity",
    "getSymbol",
    "getWWW",
    "GF",
    "globalAssign",
    "globalAssignFunction",
    "globalAssignment",
    "globalReleaseFunction",
    "gradedModule",
    "gradedModuleMap",
    "gramm",
    "graphIdeal",
    "graphRing",
    "Grassmannian",
    "groebnerBasis",
    "groupID",
    "hash",
    "hashTable",
    "heft",
    "height",
    "hermite",
    "hilbertFunction",
    "hilbertPolynomial",
    "hilbertSeries",
    "hold",
    "Hom",
    "homogenize",
    "homology",
    "homomorphism",
    "hooks",
    "horizontalJoin",
    "html",
    "httpHeaders",
    "hypertext",
    "icFracP",
    "icFractions",
    "icMap",
    "icPIdeal",
    "ideal",
    "idealizer",
    "identity",
    "image",
    "imaginaryPart",
    "importFrom",
    "independentSets",
    "index",
    "indices",
    "inducedMap",
    "inducesWellDefinedMap",
    "info",
    "input",
    "insert",
    "installAssignmentMethod",
    "installedPackages",
    "installHilbertFunction",
    "installMethod",
    "installMinprimes",
    "installPackage",
    "instance",
    "instances",
    "integralClosure",
    "integrate",
    "intersect",
    "intersectInP",
    "intersection",
    "interval",
    "inverse",
    "inverseErf",
    "inversePermutation",
    "inverseRegularizedBeta",
    "inverseRegularizedGamma",
    "inverseSystem",
    "irreducibleCharacteristicSeries",
    "irreducibleDecomposition",
    "isAffineRing",
    "isANumber",
    "isBorel",
    "isc",
    "isCanceled",
    "isCommutative",
    "isConstant",
    "isDirectory",
    "isDirectSum",
    "isEmpty",
    "isField",
    "isFinite",
    "isFinitePrimeField",
    "isFreeModule",
    "isGlobalSymbol",
    "isHomogeneous",
    "isIdeal",
    "isInfinite",
    "isInjective",
    "isInputFile",
    "isIsomorphic",
    "isIsomorphism",
    "isLinearType",
    "isListener",
    "isLLL",
    "isMember",
    "isModule",
    "isMonomialIdeal",
    "isNormal",
    "isOpen",
    "isOutputFile",
    "isPolynomialRing",
    "isPrimary",
    "isPrime",
    "isPrimitive",
    "isPseudoprime",
    "isQuotientModule",
    "isQuotientOf",
    "isQuotientRing",
    "isReady",
    "isReal",
    "isReduction",
    "isRegularFile",
    "isRing",
    "isSkewCommutative",
    "isSorted",
    "isSquareFree",
    "isStandardGradedPolynomialRing",
    "isSubmodule",
    "isSubquotient",
    "isSubset",
    "isSupportedInZeroLocus",
    "isSurjective",
    "isTable",
    "isUnit",
    "isWellDefined",
    "isWeylAlgebra",
    "jacobian",
    "jacobianDual",
    "join",
    "ker",
    "kernel",
    "kernelLLL",
    "kernelOfLocalization",
    "keys",
    "kill",
    "koszul",
    "last",
    "lcm",
    "leadCoefficient",
    "leadComponent",
    "leadMonomial",
    "leadTerm",
    "left",
    "length",
    "letterParser",
    "lift",
    "liftable",
    "limitFiles",
    "limitProcesses",
    "lines",
    "linkFile",
    "listForm",
    "listSymbols",
    "LLL",
    "lngamma",
    "load",
    "loadPackage",
    "localDictionaries",
    "localize",
    "locate",
    "log",
    "log1p",
    "lookup",
    "lookupCount",
    "LUdecomposition",
    "M2CODE",
    "makeDirectory",
    "makeDocumentTag",
    "makePackageIndex",
    "makeS2",
    "map",
    "markedGB",
    "match",
    "mathML",
    "matrix",
    "max",
    "maxPosition",
    "member",
    "memoize",
    "memoizeClear",
    "memoizeValues",
    "merge",
    "mergePairs",
    "method",
    "methodOptions",
    "methods",
    "midpoint",
    "min",
    "mingens",
    "mingle",
    "minimalBetti",
    "minimalPresentation",
    "minimalPrimes",
    "minimalReduction",
    "minimizeFilename",
    "minors",
    "minPosition",
    "minPres",
    "minprimes",
    "minus",
    "mkdir",
    "mod",
    "module",
    "modulo",
    "monoid",
    "monomialCurveIdeal",
    "monomialIdeal",
    "monomials",
    "monomialSubideal",
    "moveFile",
    "multidegree",
    "multidoc",
    "multigraded",
    "multiplicity",
    "mutable",
    "mutableIdentity",
    "mutableMatrix",
    "nanosleep",
    "needs",
    "needsPackage",
    "net",
    "netList",
    "newClass",
    "newCoordinateSystem",
    "newNetFile",
    "newPackage",
    "newRing",
    "nextkey",
    "nextPrime",
    "NNParser",
    "nonspaceAnalyzer",
    "norm",
    "normalCone",
    "notImplemented",
    "nullhomotopy",
    "nullParser",
    "nullSpace",
    "number",
    "numcols",
    "numColumns",
    "numerator",
    "numeric",
    "numericInterval",
    "numgens",
    "numRows",
    "numrows",
    "odd",
    "oeis",
    "ofClass",
    "on",
    "openDatabase",
    "openDatabaseOut",
    "openFiles",
    "openIn",
    "openInOut",
    "openListener",
    "openOut",
    "openOutAppend",
    "optionalSignParser",
    "options",
    "optP",
    "orP",
    "override",
    "pack",
    "package",
    "packageTemplate",
    "pad",
    "pager",
    "pairs",
    "parent",
    "part",
    "partition",
    "partitions",
    "parts",
    "pdim",
    "peek",
    "permanents",
    "permutations",
    "pfaffians",
    "pivots",
    "plus",
    "poincare",
    "poincareN",
    "polarize",
    "poly",
    "position",
    "positions",
    "power",
    "powermod",
    "precision",
    "preimage",
    "prepend",
    "presentation",
    "pretty",
    "primaryComponent",
    "primaryDecomposition",
    "print",
    "printerr",
    "printString",
    "processID",
    "product",
    "profile",
    "Proj",
    "projectiveHilbertPolynomial",
    "promote",
    "protect",
    "prune",
    "pseudocode",
    "pseudoRemainder",
    "pushForward",
    "QQParser",
    "QRDecomposition",
    "quotient",
    "quotientRemainder",
    "radical",
    "radicalContainment",
    "random",
    "randomKRationalPoint",
    "randomMutableMatrix",
    "rank",
    "read",
    "readDirectory",
    "readlink",
    "readPackage",
    "realPart",
    "realpath",
    "recursionDepth",
    "reducedRowEchelonForm",
    "reduceHilbert",
    "reductionNumber",
    "reesAlgebra",
    "reesAlgebraIdeal",
    "reesIdeal",
    "regex",
    "regexQuote",
    "registerFinalizer",
    "regSeqInIdeal",
    "regularity",
    "regularizedBeta",
    "regularizedGamma",
    "relations",
    "relativizeFilename",
    "remainder",
    "remove",
    "removeDirectory",
    "removeFile",
    "removeLowestDimension",
    "reorganize",
    "replace",
    "res",
    "reshape",
    "resolution",
    "resultant",
    "reverse",
    "right",
    "ring",
    "ringFromFractions",
    "roots",
    "rotate",
    "round",
    "rowAdd",
    "rowMult",
    "rowPermute",
    "rowRankProfile",
    "rowSwap",
    "rsort",
    "run",
    "runHooks",
    "runLengthEncode",
    "runProgram",
    "same",
    "saturate",
    "scan",
    "scanKeys",
    "scanLines",
    "scanPairs",
    "scanValues",
    "schedule",
    "schreyerOrder",
    "Schubert",
    "searchPath",
    "sec",
    "sech",
    "seeParsing",
    "select",
    "selectInSubring",
    "selectVariables",
    "separate",
    "separateRegexp",
    "sequence",
    "serialNumber",
    "set",
    "setEcho",
    "setGroupID",
    "setIOExclusive",
    "setIOSynchronized",
    "setIOUnSynchronized",
    "setRandomSeed",
    "setup",
    "setupEmacs",
    "sheaf",
    "sheafHom",
    "show",
    "showHtml",
    "showTex",
    "simpleDocFrob",
    "sin",
    "singularLocus",
    "sinh",
    "size",
    "size2",
    "sleep",
    "smithNormalForm",
    "solve",
    "someTerms",
    "sort",
    "sortColumns",
    "source",
    "span",
    "Spec",
    "specialFiber",
    "specialFiberIdeal",
    "splice",
    "splitWWW",
    "sqrt",
    "stack",
    "stacksProject",
    "standardForm",
    "standardPairs",
    "stashValue",
    "status",
    "style",
    "sub",
    "sublists",
    "submatrix",
    "submatrixByDegrees",
    "subquotient",
    "subsets",
    "substitute",
    "substring",
    "subtable",
    "sum",
    "super",
    "support",
    "SVD",
    "switch",
    "sylvesterMatrix",
    "symbolBody",
    "symlinkDirectory",
    "symlinkFile",
    "symmetricAlgebra",
    "symmetricAlgebraIdeal",
    "symmetricKernel",
    "symmetricPower",
    "synonym",
    "SYNOPSIS",
    "syz",
    "syzygyScheme",
    "table",
    "take",
    "tally",
    "tan",
    "tangentCone",
    "tangentSheaf",
    "tanh",
    "target",
    "taskResult",
    "temporaryFileName",
    "tensor",
    "tensorAssociativity",
    "terminalParser",
    "terms",
    "TEST",
    "testHunekeQuestion",
    "tests",
    "tex",
    "texMath",
    "times",
    "toAbsolutePath",
    "toCC",
    "toDividedPowers",
    "toDual",
    "toExternalString",
    "toField",
    "toList",
    "toLower",
    "top",
    "topCoefficients",
    "topComponents",
    "toRR",
    "toRRi",
    "toSequence",
    "toString",
    "toUpper",
    "trace",
    "transpose",
    "trim",
    "truncate",
    "truncateOutput",
    "tutorial",
    "ultimate",
    "unbag",
    "uncurry",
    "undocumented",
    "uniform",
    "uninstallAllPackages",
    "uninstallPackage",
    "unique",
    "uniquePermutations",
    "unsequence",
    "unstack",
    "urlEncode",
    "use",
    "userSymbols",
    "utf8",
    "utf8check",
    "validate",
    "value",
    "values",
    "variety",
    "vars",
    "vector",
    "versalEmbedding",
    "wait",
    "wedgeProduct",
    "weightRange",
    "whichGm",
    "width",
    "wikipedia",
    "wrap",
    "youngest",
    "zero",
    "zeta",
    "ZZParser"
    )

M2CONSTANTS = (
    "AbstractToricVarieties",
    "Acknowledgement",
    "AdditionalPaths",
    "AdjointIdeal",
    "AfterEval",
    "AfterNoPrint",
    "AfterPrint",
    "AInfinity",
    "AlgebraicSplines",
    "Algorithm",
    "Alignment",
    "AllCodimensions",
    "allowableThreads",
    "AnalyzeSheafOnP1",
    "applicationDirectorySuffix",
    "argument",
    "Ascending",
    "AssociativeAlgebras",
    "Authors",
    "AuxiliaryFiles",
    "backtrace",
    "Bareiss",
    "BaseFunction",
    "baseRings",
    "BaseRow",
    "BasisElementLimit",
    "Bayer",
    "BeforePrint",
    "BeginningMacaulay2",
    "Benchmark",
    "Bertini",
    "BettiCharacters",
    "BGG",
    "BIBasis",
    "Binary",
    "Binomial",
    "BinomialEdgeIdeals",
    "Binomials",
    "BKZ",
    "BlockMatrix",
    "Body",
    "BoijSoederberg",
    "Book3264Examples",
    "BooleanGB",
    "Boxes",
    "Browse",
    "Bruns",
    "cache",
    "CacheExampleOutput",
    "CallLimit",
    "CannedExample",
    "CatalanConstant",
    "Caveat",
    "Center",
    "Certification",
    "ChainComplexExtras",
    "ChainComplexOperations",
    "ChangeMatrix",
    "CharacteristicClasses",
    "CheckDocumentation",
    "Chordal",
    "Classic",
    "clearAll",
    "clearOutput",
    "close",
    "closeIn",
    "closeOut",
    "ClosestFit",
    "Code",
    "CodimensionLimit",
    "CodingTheory",
    "CoefficientRing",
    "Cofactor",
    "CohenEngine",
    "CohenTopLevel",
    "CohomCalg",
    "CoincidentRootLoci",
    "commandLine",
    "CompactMatrix",
    "compactMatrixForm",
    "Complement",
    "CompleteIntersection",
    "CompleteIntersectionResolutions",
    "Complexes",
    "ConductorElement",
    "Configuration",
    "ConformalBlocks",
    "Consequences",
    "Constants",
    "Contributors",
    "ConvexInterface",
    "ConwayPolynomials",
    "copyright",
    "Core",
    "CorrespondenceScrolls",
    "CotangentSchubert",
    "Cremona",
    "currentFileDirectory",
    "currentFileName",
    "currentLayout",
    "currentPackage",
    "Cyclotomic",
    "Date",
    "dd",
    "DebuggingMode",
    "debuggingMode",
    "debugLevel",
    "DecomposableSparseSystems",
    "Decompose",
    "Default",
    "defaultPrecision",
    "Degree",
    "DegreeLift",
    "DegreeLimit",
    "DegreeMap",
    "DegreeOrder",
    "DegreeRank",
    "Degrees",
    "Dense",
    "Density",
    "Depth",
    "Descending",
    "Description",
    "DeterminantalRepresentations",
    "DGAlgebras",
    "dictionaryPath",
    "DiffAlg",
    "Dispatch",
    "DivideConquer",
    "DividedPowers",
    "Divisor",
    "Dmodules",
    "docExample",
    "docTemplate",
    "Down",
    "EagonResolution",
    "EdgeIdeals",
    "edit",
    "EigenSolver",
    "EisenbudHunekeVasconcelos",
    "Elimination",
    "EliminationMatrices",
    "EllipticCurves",
    "EllipticIntegrals",
    "Email",
    "end",
    "endl",
    "Engine",
    "engineDebugLevel",
    "EngineTests",
    "EnumerationCurves",
    "environment",
    "EquivariantGB",
    "errorDepth",
    "EulerConstant",
    "Example",
    "ExampleFiles",
    "ExampleSystems",
    "Exclude",
    "exit",
    "Ext",
    "ExteriorIdeals",
    "ExteriorModules",
    "false",
    "FastMinors",
    "FastNonminimal",
    "FGLM",
    "fileDictionaries",
    "fileExitHooks",
    "FileName",
    "FindOne",
    "FiniteFittingIdeals",
    "First",
    "FirstPackage",
    "FlatMonoid",
    "Flexible",
    "flush",
    "FollowLinks",
    "FormalGroupLaws",
    "Format",
    "FourierMotzkin",
    "FourTiTwo",
    "fpLLL",
    "FrobeniusThresholds",
    "FunctionFieldDesingularization",
    "GBDegrees",
    "gbTrace",
    "GenerateAssertions",
    "Generic",
    "GenericInitialIdeal",
    "gfanInterface",
    "Givens",
    "GKMVarieties",
    "GLex",
    "Global",
    "GlobalAssignHook",
    "globalAssignmentHooks",
    "GlobalHookStore",
    "GlobalReleaseHook",
    "Gorenstein",
    "GradedLieAlgebras",
    "GraphicalModels",
    "GraphicalModelsMLE",
    "Graphics",
    "Graphs",
    "GRevLex",
    "GroebnerStrata",
    "GroebnerWalk",
    "GroupLex",
    "GroupRevLex",
    "GTZ",
    "Hadamard",
    "handleInterrupts",
    "HardDegreeLimit",
    "Heading",
    "Headline",
    "Heft",
    "Height",
    "help",
    "Hermite",
    "Hermitian",
    "HH",
    "hh",
    "HigherCIOperators",
    "HighestWeights",
    "Hilbert",
    "HodgeIntegrals",
    "homeDirectory",
    "HomePage",
    "Homogeneous",
    "Homogeneous2",
    "HomotopyLieAlgebra",
    "HorizontalSpace",
    "HyperplaneArrangements",
    "id",
    "IgnoreExampleErrors",
    "ii",
    "incomparable",
    "Increment",
    "indeterminate",
    "Index",
    "indexComponents",
    "infinity",
    "InfoDirSection",
    "infoHelp",
    "Inhomogeneous",
    "Inputs",
    "InstallPrefix",
    "IntegralClosure",
    "interpreterDepth",
    "Intersection",
    "InvariantRing",
    "InverseMethod",
    "Inverses",
    "InverseSystems",
    "Invertible",
    "InvolutiveBases",
    "Isomorphism",
    "Item",
    "Iterate",
    "Jacobian",
    "Jets",
    "Join",
    "Jupyter",
    "K3Carpets",
    "K3Surfaces",
    "Keep",
    "KeepFiles",
    "KeepZeroes",
    "Key",
    "Keywords",
    "Kronecker",
    "KustinMiller",
    "lastMatch",
    "LatticePolytopes",
    "Layout",
    "Left",
    "LengthLimit",
    "Lex",
    "LexIdeals",
    "Licenses",
    "LieTypes",
    "Limit",
    "Linear",
    "LinearAlgebra",
    "LinearTruncations",
    "lineNumber",
    "listLocalSymbols",
    "listUserSymbols",
    "LLLBases",
    "loadDepth",
    "LoadDocumentation",
    "loadedFiles",
    "loadedPackages",
    "Local",
    "LocalRings",
    "LongPolynomial",
    "M0nbar",
    "Macaulay2Doc",
    "MakeDocumentation",
    "MakeHTML",
    "MakeInfo",
    "MakeLinks",
    "MakePDF",
    "MapleInterface",
    "Markov",
    "Matroids",
    "maxAllowableThreads",
    "maxExponent",
    "MaximalRank",
    "MaxReductionCount",
    "MCMApproximations",
    "MergeTeX",
    "minExponent",
    "MinimalGenerators",
    "MinimalMatrix",
    "minimalPresentationMap",
    "minimalPresentationMapInv",
    "MinimalPrimes",
    "Minimize",
    "MinimumVersion",
    "Miura",
    "MixedMultiplicity",
    "ModuleDeformations",
    "MonodromySolver",
    "Monomial",
    "MonomialAlgebras",
    "MonomialIntegerPrograms",
    "MonomialOrbits",
    "MonomialOrder",
    "Monomials",
    "MonomialSize",
    "MultiGradedRationalMap",
    "MultiplicitySequence",
    "MultiplierIdeals",
    "MultiplierIdealsDim2",
    "MultiprojectiveVarieties",
    "NAGtypes",
    "Name",
    "Nauty",
    "NautyGraphs",
    "NCAlgebra",
    "NCLex",
    "NewFromMethod",
    "newline",
    "NewMethod",
    "NewOfFromMethod",
    "NewOfMethod",
    "nil",
    "Node",
    "NoetherianOperators",
    "NoetherNormalization",
    "NonminimalComplexes",
    "NoPrint",
    "Normaliz",
    "NormalToricVarieties",
    "notify",
    "NTL",
    "null",
    "nullaryMethods",
    "NumericalAlgebraicGeometry",
    "NumericalCertification",
    "NumericalImplicitization",
    "NumericalLinearAlgebra",
    "NumericalSchubertCalculus",
    "NumericSolutions",
    "OldPolyhedra",
    "OldToricVectorBundles",
    "OnlineLookup",
    "OO",
    "oo",
    "ooo",
    "oooo",
    "OpenMath",
    "operatorAttributes",
    "OptionalComponentsPresent",
    "Options",
    "Order",
    "order",
    "OutputDictionary",
    "Outputs",
    "PackageCitations",
    "PackageDictionary",
    "PackageExports",
    "PackageImports",
    "PackageTemplate",
    "PairLimit",
    "PairsRemaining",
    "Parametrization",
    "Parsing",
    "path",
    "PencilsOfQuadrics",
    "Permanents",
    "PHCpack",
    "PhylogeneticTrees",
    "pi",
    "PieriMaps",
    "PlaneCurveSingularities",
    "Points",
    "Polyhedra",
    "Polymake",
    "Posets",
    "Position",
    "PositivityToricBundles",
    "POSIX",
    "Postfix",
    "Pre",
    "Precision",
    "Prefix",
    "prefixDirectory",
    "prefixPath",
    "PrimaryDecomposition",
    "PrimaryTag",
    "PrimitiveElement",
    "Print",
    "printingAccuracy",
    "printingLeadLimit",
    "printingPrecision",
    "printingSeparator",
    "printingTimeLimit",
    "printingTrailLimit",
    "printWidth",
    "Probability",
    "profileSummary",
    "programPaths",
    "Projective",
    "Prune",
    "PruneComplex",
    "pruningMap",
    "Pullback",
    "PushForward",
    "Python",
    "QthPower",
    "Quasidegrees",
    "QuaternaryQuartics",
    "QuillenSuslin",
    "quit",
    "Quotient",
    "Radical",
    "RadicalCodim1",
    "RaiseError",
    "RandomCanonicalCurves",
    "RandomComplexes",
    "RandomCurves",
    "RandomCurvesOverVerySmallFiniteFields",
    "RandomGenus14Curves",
    "RandomIdeals",
    "RandomMonomialIdeals",
    "RandomObjects",
    "RandomPlaneCurves",
    "RandomPoints",
    "RandomSpaceCurves",
    "Range",
    "RationalMaps",
    "RationalPoints",
    "RationalPoints2",
    "ReactionNetworks",
    "RealFP",
    "RealQP",
    "RealQP1",
    "RealRoots",
    "RealRR",
    "RealXD",
    "recursionLimit",
    "Reduce",
    "ReesAlgebra",
    "References",
    "ReflexivePolytopesDB",
    "Regularity",
    "RelativeCanonicalResolution",
    "Reload",
    "RemakeAllDocumentation",
    "RerunExamples",
    "ResidualIntersections",
    "ResLengthThree",
    "ResolutionsOfStanleyReisnerRings",
    "restart",
    "Result",
    "Resultants",
    "returnCode",
    "Reverse",
    "RevLex",
    "Right",
    "rootPath",
    "rootURI",
    "RunDirectory",
    "RunExamples",
    "RunExternalM2",
    "Saturation",
    "Schubert2",
    "SchurComplexes",
    "SchurFunctors",
    "SchurRings",
    "scriptCommandLine",
    "SCSCP",
    "SectionRing",
    "SeeAlso",
    "SegreClasses",
    "SemidefiniteProgramming",
    "Seminormalization",
    "SeparateExec",
    "Serialization",
    "sheafExt",
    "ShimoyamaYokoyama",
    "showClassStructure",
    "showStructure",
    "showUserStructure",
    "SimpleDoc",
    "SimplicialComplexes",
    "SimplicialDecomposability",
    "SimplicialPosets",
    "SimplifyFractions",
    "SizeLimit",
    "SkewCommutative",
    "SlackIdeals",
    "SLnEquivariantMatrices",
    "SLPexpressions",
    "Sort",
    "SortStrategy",
    "SourceCode",
    "SourceRing",
    "SpaceCurves",
    "SparseResultants",
    "SpechtModule",
    "SpecialFanoFourfolds",
    "SpectralSequences",
    "SRdeformations",
    "Standard",
    "StartWithOneMinor",
    "StatePolytope",
    "StatGraphs",
    "stderr",
    "stdio",
    "StopBeforeComputation",
    "stopIfError",
    "StopWithMinimalGenerators",
    "Strategy",
    "Strict",
    "StronglyStableIdeals",
    "Style",
    "SubalgebraBases",
    "Subnodes",
    "SubringLimit",
    "subscript",
    "Sugarless",
    "SumsOfSquares",
    "SuperLinearAlgebra",
    "superscript",
    "SVDComplexes",
    "SwitchingFields",
    "SymbolicPowers",
    "SymmetricPolynomials",
    "Synopsis",
    "Syzygies",
    "SyzygyLimit",
    "SyzygyMatrix",
    "SyzygyRows",
    "TangentCone",
    "TateOnProducts",
    "TensorComplexes",
    "Test",
    "testExample",
    "TestIdeals",
    "TeXmacs",
    "Text",
    "ThinSincereQuivers",
    "ThreadedGB",
    "Threshold",
    "Topcom",
    "topLevelMode",
    "Tor",
    "TorAlgebra",
    "Toric",
    "ToricInvariants",
    "ToricTopology",
    "ToricVectorBundles",
    "TotalPairs",
    "Tree",
    "TriangularSets",
    "Tries",
    "Trim",
    "Triplets",
    "Tropical",
    "true",
    "Truncate",
    "Truncations",
    "TSpreadIdeals",
    "TypicalValue",
    "typicalValues",
    "Undo",
    "Unique",
    "Units",
    "Unmixed",
    "Up",
    "UpdateOnly",
    "UpperTriangular",
    "Usage",
    "UseCachedExampleOutput",
    "UseHilbertFunction",
    "UserMode",
    "UseSyzygies",
    "Variable",
    "VariableBaseName",
    "Variables",
    "Vasconcelos",
    "VectorFields",
    "VectorGraphics",
    "Verbose",
    "Verbosity",
    "Verify",
    "VersalDeformations",
    "Version",
    "version",
    "VerticalSpace",
    "viewHelp",
    "VirtualResolutions",
    "Visualize",
    "WebApp",
    "Weights",
    "WeylAlgebra",
    "WeylGroups",
    "Wrap",
    "XML"
    )

class Macaulay2Lexer(RegexLexer):
    """Lexer for Macaulay2, a software system for research in algebraic geometry."""

    name = 'Macaulay2'
    url = 'https://faculty.math.illinois.edu/Macaulay2/'
    aliases = ['macaulay2']
    filenames = ['*.m2']

    tokens = {
        'root': [
            (r'--.*$', Comment.Single),
            (r'-\*', Comment.Multiline, 'block comment'),
            (r'"', String, 'quote string'),
            (r'///', String, 'slash string'),
            (words(M2KEYWORDS, prefix=r'\b', suffix=r'\b'), Keyword),
            (words(M2DATATYPES, prefix=r'\b', suffix=r'\b'), Name.Builtin),
            (words(M2FUNCTIONS, prefix=r'\b', suffix=r'\b'), Name.Function),
            (words(M2CONSTANTS, prefix=r'\b', suffix=r'\b'), Name.Constant),
            (r'\s+', Text.Whitespace),
            (r'.', Text)
        ],
        'block comment' : [
            (r'[^*-]+', Comment.Multiline),
            (r'\*-', Comment.Multiline, '#pop'),
            (r'[*-]', Comment.Multiline)
        ],
        'quote string' : [
            (r'[^\\"]+', String),
            (r'"', String, '#pop'),
            (r'\\"?', String),
        ],
        'slash string' : [
            (r'[^/]+', String),
            (r'(//)+(?!/)', String),
            (r'/(//)+(?!/)', String, '#pop'),
            (r'/', String)
        ]
    }
