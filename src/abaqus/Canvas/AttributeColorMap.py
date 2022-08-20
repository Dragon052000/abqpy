from ..UtilityAndView.abaqusConstants import *
from .._OptionsBase import _OptionsBase
from .._decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class AttributeColorMap(_OptionsBase):
    """The AttributeColorMap object is used to store values and attributes associated with
    AttributeColorMap type objects. AttributeColorMap objects can be modified using the
    methods described below. The methods accessed via the Viewport object cause the
    AttributeColorMap object to be updated in the session.viewports[name].colorMappings
    repository.

    .. note::
        This object can be accessed by:

        .. code-block:: python

            session.viewports[name].colorMappings[name]
    """

    #: A SymbolicConstant specifying the type of AttributeColorMap . Possible values are
    #: MATERIAL_MAP, SECTION_MAP, PART_MAP, ELSET_MAP, AVERAGING_REGION_MAP, and ELTYPE_MAP.
    mapType: SymbolicConstant = None

    #: A Dictionary object specifying a color mapping. Each key is of String type and specifies
    #: an attribute in the map; the corresponding values specify the color definition to apply
    #: to that attribute in the form (0|1, wire color, edge color, face color). The 0|1 defines
    #: the active status for the attribute. For example:
    # `overrides = {'Part-1':(1,'#00FF00', '#00CCFF', '#00FF00')}`
    overrides: dict = None

    #: A Dictionary object specifying a custom color mapping similar to overrides. For
    #: example: `defaultOverrides = {'Copper':(1,''#00FF00', '#00CCFF', '#00FF00')}`
    #: The color mapping can contain keys that have not been
    #: created. When the key is created, it gets the appropriate values from this mapping.
    defaultOverrides: dict = None

    #: A Dictionary object specifying the color settings of each attribute as described in the
    #: :meth:`abaqus.Canvas.AttributeColorMap.updateOverrides` method.
    attributeColors: dict = None

    @abaqus_method_doc
    def setDefaults(self):
        """This method resets the AttributeColorMap object to its default state."""
        #: TODO: Implement this method.
        ...

    @abaqus_method_doc
    def setValues(self, overrides: dict = None, defaultOverrides: dict = None):
        """This method modifies the AttributeColorMap object.

        Parameters
        ----------
        overrides
            A Dictionary object specifying a color mapping. Each key is of String type and specifies
            an attribute in the map; the corresponding values specify the color definition to apply
            to that attribute in the form (0|1, wire color, edge color, face color). The 0|1 defines
            the active status for the attribute. For example:
            `overrides = {'Part-1':(1,'#00FF00', '#00CCFF', '#00FF00')}`
        defaultOverrides
            A Dictionary object specifying a custom color mapping similar to overrides. For
            example: `defaultOverrides = {'Copper':(1,''#00FF00', '#00CCFF', '#00FF00')}`.
            The color mapping can contain keys that have not been
            created. When the key is created, it gets the appropriate values from this mapping.
        """
        super().setValues(overrides=overrides, defaultOverrides=defaultOverrides)

    @abaqus_method_doc
    def updateOverrides(self, overrides: dict = None, defaultOverrides: dict = None):
        """This method specifies additional overrides to be added to the current object definition.

        Parameters
        ----------
        overrides
            A Dictionary object specifying a color mapping. Each key is of String type and specifies
            an attribute in the map; the corresponding values specify the color definition to apply
            to that attribute in the form (0|1, wire color, edge color, face color). The 0|1 defines
            the active status for the attribute. For example:
            `overrides = {'Part-1':(1,'#00FF00', '#00CCFF', '#00FF00')}`
        defaultOverrides
            A Dictionary object specifying a custom color mapping similar to overrides. For
            example: `defaultOverrides={'Copper':(1,''#00FF00', '#00CCFF', '#00FF00')}`
            The color mapping can contain keys that have not been
            created. When the key is created, it gets the appropriate values from this mapping.
        """
        #: TODO: Implement this method.
        ...
