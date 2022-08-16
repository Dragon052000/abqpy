from .Section import Section
from ..UtilityAndView.abaqusConstants import *


class MPCSection(Section):
    """The MPCSection object defines the properties of a multi-point constraint section.
    The MPCSection object is derived from the Section object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]

        The corresponding analysis keywords are:

        - MPC
    """

    #: A String specifying the repository key.
    name: str

    #: A SymbolicConstant specifying the MPC type of the section. Possible values are BEAM_MPC,
    #: ELBOW_MPC, PIN_MPC, LINK_MPC, TIE_MPC, and USER_DEFINED.
    mpcType: SymbolicConstant

    #: A SymbolicConstant specifying the mode of the MPC when it is user-defined. Possible
    #: values are DOF_MODE and NODE_MODE. The default value is DOF_MODE.The **userMode** argument
    #: applies only when **mpcType** = USER_DEFINED.
    userMode: SymbolicConstant = DOF_MODE

    #: An Int specifying to differentiate between different constraint types in a user-defined
    #: MPCSection. The default value is 0.The **userType** argument applies only when
    #: **mpcType** = USER_DEFINED.
    userType: int = 0

    def __init__(
        self,
        name: str,
        mpcType: SymbolicConstant,
        userMode: SymbolicConstant = DOF_MODE,
        userType: int = 0,
    ):
        """This method creates a MPCSection object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].MPCSection
                session.odbs[name].MPCSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        mpcType
            A SymbolicConstant specifying the MPC type of the section. Possible values are BEAM_MPC,
            ELBOW_MPC, PIN_MPC, LINK_MPC, TIE_MPC, and USER_DEFINED.
        userMode
            A SymbolicConstant specifying the mode of the MPC when it is user-defined. Possible
            values are DOF_MODE and NODE_MODE. The default value is DOF_MODE.The **userMode** argument
            applies only when **mpcType** = USER_DEFINED.
        userType
            An Int specifying to differentiate between different constraint types in a user-defined
            MPCSection. The default value is 0.The **userType** argument applies only when
            **mpcType** = USER_DEFINED.

        Returns
        -------
        MPCSection
            A :py:class:`~abaqus.Section.MPCSection.MPCSection` object.

        Raises
        ------
        RangeError and InvalidNameError
        """
        super().__init__()
