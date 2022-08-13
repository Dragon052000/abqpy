from abaqusConstants import *
import typing

from .CaeGuiPrefs import CaeGuiPrefs
from .CaeKerPrefs import CaeKerPrefs

"""The Python module caePrefsAccess contains functions that enable you to edit the 
Abaqus/CAE preferences file, abaqus_2021.gpr. 

.. note:: 
    This object can be accessed by:

    .. code-block:: python

        import caePrefsAccess

"""


def getGuiPrefsFileName() -> str:
    """This function enables you to retrieve the location of your abaqus_2021.gpr file.

    .. note:: 
        This function can be accessed by:

        .. code-block:: python

            caePrefsAccess.getGuiPrefsFileName

    Returns
    -------
    str
        A String with the default file name for the GUI preferences file.
    """
    # TODO: Implement this function
    ...


def getDisplayNamesInGuiPreferences(fileName: str) -> list[str]:
    """The abaqus_2021.gpr file stores a separate guiPreferences record for each display that
    you use. This function returns a list of every displayName recorded in the preferences
    file.

    .. note:: 
        This function can be accessed by:

        .. code-block:: python

            caePrefsAccess.getDisplayNamesInGuiPreferences

    Parameters
    ----------
    fileName: str
        A String that specifies the path to the preferences file.

    Returns
    -------
    list[str]
        A list of Strings of displayNames.
    """
    # TODO: Implement this function
    ...


def printValuesList(
    object: str,
    maxRecursionDepth: typing.Union[int, typing.Literal["UNLIMITED"]] = None,
    asString: Boolean = False,
) -> str:
    """This function enables you to print all of the options and their values for a set of
    guiPreferences or sessionOptions settings derived from the abaqus_2021.gpr file.

    .. note:: 
            This function can be accessed by:

            .. code-block:: python

                caePrefsAccess.printValuesList

    Parameters
    ----------
    object: str
        The guiPreferences object or sessionOptions object for which you want to print options
        and their values.
    maxRecursionDepth: typing.Union[int, typing.Literal['UNLIMITED']]
        An Int, or SymbolicConstant UNLIMITED, that specifies the depth of recursion when
        accessing the attributes of **object**.
    asString: Boolean
        A Boolean specifying how the string representation of each option is printed. If
        **asString** is True, printValuesList prints the str of each option; otherwise
        printValuesList prints the repr of the options. The default value is False.

    Returns
    -------
    str
        A String displaying the path, name, and value for all of the options in the object that
        you select.
    """
    # TODO: Implement this function
    ...


def openGuiPreferences(displayName: str, fileName: str = "") -> CaeGuiPrefs:
    """This function enables you to examine and change many default behaviors in the Abaqus/CAE
    graphical user interface. Abaqus stores preferences for each display you use in a
    separate guiPreferences section of the abaqus_2021.gpr file.

    .. note:: 
        This function can be accessed by:

        .. code-block:: python

            caePrefsAccess.openGuiPreferences

    Parameters
    ----------
    displayName: str
        A String that specifies the display for which you want to investigate GUI preferences
        from the abaqus_2021.gpr file. You can retrieve the available display names in the file
        by using the getDisplayNamesInGuiPreferences method.
    fileName: str
        A String specifying the path to the preferences file. The openGuiPreferences method uses
        this argument if you are working with a preferences file that is not at the default
        location.If this argument is omitted, the abaqus_2021.gpr file in your home directory is
        opened.

    Returns
    -------
    CaeGuiPrefs
        A :py:class:`~abaqus.AbaqusCAEDisplayPreferences.CaeGuiPrefs.CaeGuiPrefs` object.
    """
    return CaeGuiPrefs()


def openSessionOptions(
    fileName: str = "", directory: typing.Literal["CURRENT", "HOME"] = HOME
) -> CaeKerPrefs:
    """This function enables you to examine and change the default behavior for many session
    options Abaqus/CAE; that is, the settings that you can save in Abaqus/CAE from the
    FileSave Display ConstrainedSketchOptions menu option. Abaqus stores default session options in the
    sessionOptions section of the abaqus_2021.gpr file.

    .. note:: 
        This function can be accessed by:

        .. code-block:: python

            caePrefsAccess.openSessionOptions

    Parameters
    ----------
    fileName: str
        A String specifying the path to the preferences file. The openSessionOptions method uses
        this argument if you are working with a preferences file that is not at the default
        location.If this argument is omitted, the abaqus_2021.gpr file in your home directory is
        opened.
    directory: typing.Literal['CURRENT', 'HOME']
        A SymbolicConstant specifying the location of the preferences file. Possible values
        are:

        - CURRENT to open the preferences file in the current directory
          (caePrefsAccess.CURRENT)
        - HOME to open the preferences file in your home directory
          (caePrefsAccess.HOME)

        The default value is HOME. Either **fileName** or **directory** must be
        supplied. The **fileName** or **directory** arguments are mutually exclusive.

    Returns
    -------
    CaeKerPrefs
        A :py:class:`~abaqus.AbaqusCAEDisplayPreferences.CaeKerPrefs.CaeKerPrefs` object.
    """
    return CaeKerPrefs()
