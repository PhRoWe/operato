from .batch_000 import (
    Abf,
    Adyrel,
    AleGridDisp,
    AleGridDonea,
    AleGridSpring,
    AleGridStandard,
    AleGridZero,
    AleLinkOff,
    AleLinkOn,
)
from .batch_001 import (
    AleLinkVel,
    AleMusclOff,
    AleOff,
    AleOn,
    AleSolverFint,
    AleSupgOff,
    AnimBrickDama,
    AnimBrickRestype,
    AnimBrickTdel,
)
from .batch_002 import (
    AnimBrickTens,
    AnimBrickTensDama,
    AnimBrickVdami,
    AnimDt,
    AnimEltypForc,
    AnimEltypRestype,
    AnimEltypTdet,
    AnimGpsStrainTens,
    AnimGpsStressTens,
)
from .batch_003 import (
    AnimGps1,
    AnimGps2,
    AnimGzip,
    AnimLsensor,
    AnimMass,
    AnimMat,
    AnimNoda,
    AnimSensor,
    AnimShellDama,
)
from .batch_004 import (
    AnimShellEpsp,
    AnimShellFldf,
    AnimShellFldz,
    AnimShellIdply,
    AnimShellIdplyDama,
    AnimShellIdplyEpsp,
    AnimShellIdplyPhi,
    AnimShellIdplyRestype,
    AnimShellNxtfactor,
)
from .batch_005 import (
    AnimShellPhi,
    AnimShellRestype,
    AnimShellSig1h,
    AnimShellSig2h,
    AnimShellTdel,
    AnimShellTens,
    AnimTitle,
    AnimVect,
    AnimVers,
)
from .batch_006 import (
    Atfile,
    Atsymbolfile,
    AtsymbolfileKeyword2,
    BcsAle,
    BcsLag,
    BcsRot,
    BcsTra,
    BcsrAle,
    BcsrLag,
)
from .batch_007 import (
    BcsrRot,
    BcsrTra,
    Damp,
    Del,
    DelEltyp1,
    DelInter,
    Delint,
    Dt,
    DtAirbagKeyword3,
)
from .batch_008 import (
    DtAle,
    DtAms,
    DtCstAms,
    DtEltypKeyword3Iflag,
    DtFvmbagIflag,
    DtInterKeyword3Iflag,
    DtNodaKeyword3Iflag,
    DtShnodKeyword3,
    DtSphcelKeyword3,
)
from .batch_009 import (
    DtTherm,
    Dt1BrickKeyword3Iflag,
    Dt1Shell,
    Dt1tet10,
    Dtix,
    Dtsde,
    Dttsh,
    DynainDt,
    DynainShellStrainFull,
)
from .batch_010 import (
    DynainShellStressFull,
    Dyrel,
    Dyrel1,
    EndEngine,
    Funct,
    FvmbagModif,
    Fxinp,
    H3dBeam,
    H3dCompress,
)
from .batch_011 import (
    H3dDt,
    H3dLsensor,
    H3dNoda,
    H3dPart,
    H3dQuad,
    H3dRbe2SinglePart,
    H3dRbe3SinglePart,
    H3dRbodySinglePart,
    H3dShell,
)
from .batch_012 import (
    H3dSolid,
    H3dSph,
    H3dSpring,
    H3dTitle,
    H3dTruss,
    ImplAutospc,
    ImplBuckl1,
    ImplBuckl2,
    ImplCheck,
)
from .batch_013 import (
    ImplDivergN,
    ImplDt1,
    ImplDt2,
    ImplDt3,
    ImplDtFixpoint,
    ImplDtStop,
    ImplDtini,
    ImplDyna1,
    ImplDyna2,
)
from .batch_014 import (
    ImplDynaDamp,
    ImplGstifOff,
    ImplInterKcomp,
    ImplInterKnonl,
    ImplLbfgsL,
    ImplLinear,
    ImplLinearInter,
    ImplLrigrot,
    ImplLsearchOff,
)
from .batch_015 import (
    ImplLsearchN,
    ImplMonvolOff,
    ImplNcycleStop,
    ImplNonlinN,
    ImplNonlinSmdisp,
    ImplNonlinSolvinfo,
    ImplPrepat,
    ImplPrintLinear,
    ImplPrintNonlin,
)
from .batch_016 import (
    ImplPstifOff,
    ImplQstat,
    ImplQstatDtscal,
    ImplQstatMrigm,
    ImplRrefInterfN,
    ImplRrefLimit,
    ImplRrefOff,
    ImplSbcsMsglv,
    ImplSbcsOrder,
)
from .batch_017 import (
    ImplSbcsOutcore,
    ImplShpoff,
    ImplShpon,
    ImplSinit,
    ImplSolver,
    ImplSprback,
    ImplSpring,
    InivAxis,
    InivAxisKeyword31,
)
from .batch_018 import (
    InivAxisKeyword32,
    InivRot,
    InivRotKeyword31,
    InivRotKeyword32,
    InivTra,
    InivTraKeyword31,
    InivTraKeyword32,
    Inter,
    Kerel,
)
from .batch_019 import (
    Kerel1,
    Kill,
    Madymo,
    MassReset,
    Mon,
    Negvol,
    Outp,
    OutputLsensor,
    Parith,
)
from .batch_020 import (
    Print,
    Rad2radOn,
    Rbody,
    Report,
    Rerun,
    RfileOff,
    RfileN,
    Run,
    Shsub,
)
from .batch_021 import (
    StateBeamAux,
    StateBeamFull,
    StateBrickAuxFull,
    StateBrickEref,
    StateBrickFail,
    StateBrickOrtho,
    StateBrickStrainFull,
    StateBrickStrainGlobfull,
    StateBrickStresFull,
)
from .batch_022 import (
    StateBrickStresGlobfull,
    StateDt,
    StateInimap1dKeyword3,
    StateInimap2dKeyword3,
    StateLsensor,
    StateNodeBcs,
    StateNodeTemp,
    StateNodeVel,
    StateNoDel,
)
from .batch_023 import (
    StateShellAuxFull,
    StateShellEpspFull,
    StateShellFail,
    StateShellOrthl,
    StateShellStrainFull,
    StateShellStrainGlobfull,
    StateShellStressFull,
    StateShellStressGlobfull,
    StateShellThick,
)
from .batch_024 import (
    StateSpringFull,
    StateStrFile,
    StateTrussFull,
    Stop,
    StopLsensor,
    Tfile,
    ThVers,
    Thermal,
    Title,
)
from .batch_025 import (
    VelRot,
    VelTra,
    Vers,
)

# --- Build the keyword registry --------------------------------------------------------------
keywords = (
    Abf,
    Adyrel,
    AleGridDisp,
    AleGridDonea,
    AleGridSpring,
    AleGridStandard,
    AleGridZero,
    AleLinkOff,
    AleLinkOn,
    AleLinkVel,
    AleMusclOff,
    AleOff,
    AleOn,
    AleSolverFint,
    AleSupgOff,
    AnimBrickDama,
    AnimBrickRestype,
    AnimBrickTdel,
    AnimBrickTens,
    AnimBrickTensDama,
    AnimBrickVdami,
    AnimDt,
    AnimEltypForc,
    AnimEltypRestype,
    AnimEltypTdet,
    AnimGpsStrainTens,
    AnimGpsStressTens,
    AnimGps1,
    AnimGps2,
    AnimGzip,
    AnimLsensor,
    AnimMass,
    AnimMat,
    AnimNoda,
    AnimSensor,
    AnimShellDama,
    AnimShellEpsp,
    AnimShellFldf,
    AnimShellFldz,
    AnimShellIdply,
    AnimShellIdplyDama,
    AnimShellIdplyEpsp,
    AnimShellIdplyPhi,
    AnimShellIdplyRestype,
    AnimShellNxtfactor,
    AnimShellPhi,
    AnimShellRestype,
    AnimShellSig1h,
    AnimShellSig2h,
    AnimShellTdel,
    AnimShellTens,
    AnimTitle,
    AnimVect,
    AnimVers,
    Atfile,
    Atsymbolfile,
    AtsymbolfileKeyword2,
    BcsAle,
    BcsLag,
    BcsRot,
    BcsTra,
    BcsrAle,
    BcsrLag,
    BcsrRot,
    BcsrTra,
    Damp,
    Del,
    DelEltyp1,
    DelInter,
    Delint,
    Dt,
    DtAirbagKeyword3,
    DtAle,
    DtAms,
    DtCstAms,
    DtEltypKeyword3Iflag,
    DtFvmbagIflag,
    DtInterKeyword3Iflag,
    DtNodaKeyword3Iflag,
    DtShnodKeyword3,
    DtSphcelKeyword3,
    DtTherm,
    Dt1BrickKeyword3Iflag,
    Dt1Shell,
    Dt1tet10,
    Dtix,
    Dtsde,
    Dttsh,
    DynainDt,
    DynainShellStrainFull,
    DynainShellStressFull,
    Dyrel,
    Dyrel1,
    EndEngine,
    Funct,
    FvmbagModif,
    Fxinp,
    H3dBeam,
    H3dCompress,
    H3dDt,
    H3dLsensor,
    H3dNoda,
    H3dPart,
    H3dQuad,
    H3dRbe2SinglePart,
    H3dRbe3SinglePart,
    H3dRbodySinglePart,
    H3dShell,
    H3dSolid,
    H3dSph,
    H3dSpring,
    H3dTitle,
    H3dTruss,
    ImplAutospc,
    ImplBuckl1,
    ImplBuckl2,
    ImplCheck,
    ImplDivergN,
    ImplDt1,
    ImplDt2,
    ImplDt3,
    ImplDtFixpoint,
    ImplDtStop,
    ImplDtini,
    ImplDyna1,
    ImplDyna2,
    ImplDynaDamp,
    ImplGstifOff,
    ImplInterKcomp,
    ImplInterKnonl,
    ImplLbfgsL,
    ImplLinear,
    ImplLinearInter,
    ImplLrigrot,
    ImplLsearchOff,
    ImplLsearchN,
    ImplMonvolOff,
    ImplNcycleStop,
    ImplNonlinN,
    ImplNonlinSmdisp,
    ImplNonlinSolvinfo,
    ImplPrepat,
    ImplPrintLinear,
    ImplPrintNonlin,
    ImplPstifOff,
    ImplQstat,
    ImplQstatDtscal,
    ImplQstatMrigm,
    ImplRrefInterfN,
    ImplRrefLimit,
    ImplRrefOff,
    ImplSbcsMsglv,
    ImplSbcsOrder,
    ImplSbcsOutcore,
    ImplShpoff,
    ImplShpon,
    ImplSinit,
    ImplSolver,
    ImplSprback,
    ImplSpring,
    InivAxis,
    InivAxisKeyword31,
    InivAxisKeyword32,
    InivRot,
    InivRotKeyword31,
    InivRotKeyword32,
    InivTra,
    InivTraKeyword31,
    InivTraKeyword32,
    Inter,
    Kerel,
    Kerel1,
    Kill,
    Madymo,
    MassReset,
    Mon,
    Negvol,
    Outp,
    OutputLsensor,
    Parith,
    Print,
    Rad2radOn,
    Rbody,
    Report,
    Rerun,
    RfileOff,
    RfileN,
    Run,
    Shsub,
    StateBeamAux,
    StateBeamFull,
    StateBrickAuxFull,
    StateBrickEref,
    StateBrickFail,
    StateBrickOrtho,
    StateBrickStrainFull,
    StateBrickStrainGlobfull,
    StateBrickStresFull,
    StateBrickStresGlobfull,
    StateDt,
    StateInimap1dKeyword3,
    StateInimap2dKeyword3,
    StateLsensor,
    StateNodeBcs,
    StateNodeTemp,
    StateNodeVel,
    StateNoDel,
    StateShellAuxFull,
    StateShellEpspFull,
    StateShellFail,
    StateShellOrthl,
    StateShellStrainFull,
    StateShellStrainGlobfull,
    StateShellStressFull,
    StateShellStressGlobfull,
    StateShellThick,
    StateSpringFull,
    StateStrFile,
    StateTrussFull,
    Stop,
    StopLsensor,
    Tfile,
    ThVers,
    Thermal,
    Title,
    VelRot,
    VelTra,
    Vers,
)
KEYWORD_REGISTRY = {}
for keyword in keywords:
    KEYWORD_REGISTRY[keyword.__name__.upper()] = keyword
