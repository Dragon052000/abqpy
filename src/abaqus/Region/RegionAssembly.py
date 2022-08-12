import typing

from .Region import Region
from .RegionAssemblyBase import RegionAssemblyBase
from .Set import Set
from .Surface import Surface
from ..BasicGeometry.Cell import Cell
from ..BasicGeometry.Edge import Edge
from ..BasicGeometry.Face import Face
from ..BasicGeometry.ReferencePoint import ReferencePoint
from ..BasicGeometry.Vertex import Vertex
from ..Mesh.MeshElement import MeshElement
from ..Mesh.MeshNode import MeshNode


class RegionAssembly(RegionAssemblyBase):
    """An :py:class:`~abaqus.Assembly.Assembly.Assembly` object is a container for instances of parts. The Assembly object has no
    constructor command. Abaqus creates the **rootAssembly** member when a Model object is
    created.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import assembly
            mdb.models[name].rootAssembly
    """

    def Surface(
        self,
        side1Faces: tuple[Face] = None,
        side2Faces: tuple[Face] = None,
        side12Faces: tuple[Face] = None,
        end1Edges: tuple[Face] = None,
        end2Edges: tuple[Face] = None,
        circumEdges: tuple[Face] = None,
        side1Edges: tuple[Face] = None,
        side2Edges: tuple[Face] = None,
        face1Elements: tuple[Face] = None,
        face2Elements: tuple[Face] = None,
        face3Elements: tuple[Face] = None,
        face4Elements: tuple[Face] = None,
        face5Elements: tuple[Face] = None,
        face6Elements: tuple[Face] = None,
        side1Elements: tuple[Face] = None,
        side2Elements: tuple[Face] = None,
        side12Elements: tuple[Face] = None,
        end1Elements: tuple[Face] = None,
        end2Elements: tuple[Face] = None,
        circumElements: tuple[Face] = None,
        name: str = "",
    ) -> Surface:
        """This method creates a surface from a sequence of objects in a model database. The
        surface will apply to the sides specified by the arguments.For example
        surface=mdb.models['Model-1'].parts['Part-1'].Surface(side1Faces=side1Faces,
        name='Surf-1')

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].parts[name].Surface
                mdb.models[name].rootAssembly.Surface

        Parameters
        ----------
        name
            A String specifying the repository key. The default value is an empty string.
        side1Elements
            A sequence of MeshElement objects (surface applies to SIDE1 of element). 
            The default value is None.
        side2Elements
            A sequence of MeshElement objects (surface applies to SIDE2 of element). 
            The default value is None.
        side12Elements
            A sequence of MeshElement objects (surface applies to both SIDE1 and SIDE2 of element). 
            The default value is None.
        end1Elements
            A sequence of MeshElement objects (surface applies to END1 of element). 
            The default value is None.
        end2Elements
            A sequence of MeshElement objects (surface applies to END2 of element). 
            The default value is None.
        circumElements
            A sequence of MeshElement objects (surface applies to circumference of element). 
            The default value is None.
        face1Elements
            A sequence of MeshElement objects (surface applies to FACE1 of element) or MeshFace objects. 
            The default value is None.
        face2Elements
            A sequence of MeshElement objects (surface applies to FACE2 of element) or MeshFace objects. 
            The default value is None.
        face3Elements
            A sequence of MeshElement objects (surface applies to FACE3 of element) or MeshFace objects. 
            The default value is None.
        face4Elements
            A sequence of MeshElement objects (surface applies to FACE4 of element) or MeshFace objects. 
            The default value is None.
        face5Elements
            A sequence of MeshElement objects (surface applies to FACE5 of element) or MeshFace objects. 
            The default value is None.
        face6Elements
            A sequence of MeshElement objects (surface applies to FACE6 of element) or MeshFace objects. 
            The default value is None.
        side1Faces
            A sequence of Face objects (surface applies to SIDE1 of face). The default value is None.
        side2Faces
            A sequence of Face objects (surface applies to SIDE2 of face). The default value is None.
        side12Faces
            A sequence of Face objects (surface applies to both SIDE1 and SIDE2 of face). 
            The default value is None.
        side1Edges
            A sequence of Edge objects (surface applies to SIDE1 of edge). The default value is None.
        side2Edges
            A sequence of Edge objects (surface applies to SIDE2 of edge). The default value is None.
        end1Edges
            A sequence of Edge objects (surface applies to END1 of edge). The default value is None.
        end2Edges
            A sequence of Edge objects (surface applies to END2 of edge). The default value is None.
        circumEdges
            A sequence of Edge objects (surface applies circumferentially to edge). 
            The default value is None.
        kwargs
            The required parameters for different conditions are:
            
            - On three-dimensional solid faces, you can use the following arguments: 
              side1Faces, side2Faces

            - On three-dimensional shell faces, you can use the following arguments: 
              side1Faces, side2Faces, side12Faces

            - On three-dimensional wire edges, you can use the following arguments:
              end1Edges, end2Edges, circumEdges

            - On three-dimensional or two-dimensional or axisymmetric edges, you can use the following arguments:
              side1Edges, side2Edges

            - On two-dimensional or axisymmetric shell elements, you can use the following arguments:
              face1Elements, face2Elements, face3Elements, face4Elements

            - On solid elements, you can use the following arguments:
              face1Elements, face2Elements, face3Elements, face4Elements, face5Elements, face6Elements

            - On three-dimensional shell elements, you can use the following arguments:
              side1Elements, side2Elements, side12Elements

            - On three-dimensional wire elements, you can use the following arguments:
              end1Elements, end2Elements, circumElements

            - On two-dimensional or axisymmetric wire elements, you can use the following arguments:
              side1Elements, side2Elements

        Returns
        -------
        Surface
            A :py:class:`~abaqus.Region.Surface.Surface` object.
        """
        surface = Surface(
            side1Faces,
            side2Faces,
            side12Faces,
            end1Edges,
            end2Edges,
            circumEdges,
            side1Edges,
            side2Edges,
            face1Elements,
            face2Elements,
            face3Elements,
            face4Elements,
            face5Elements,
            face6Elements,
            side1Elements,
            side2Elements,
            side12Elements,
            end1Elements,
            end2Elements,
            circumElements,
            name,
        )
        self.surfaces[name] = surface
        self.allSurfaces[name] = surface
        return surface

    @typing.overload
    def Set(
        self,
        name: str,
        nodes: tuple[MeshNode] = None,
        elements: tuple[MeshElement] = None,
        region: Region = None,
        vertices: tuple[Vertex] = None,
        edges: tuple[Edge] = None,
        faces: tuple[Face] = None,
        cells: tuple[Cell] = None,
        xVertices: tuple[Vertex] = None,
        xEdges: tuple[Edge] = None,
        xFaces: tuple[Face] = None,
        referencePoints: tuple[ReferencePoint] = (),
        skinFaces: tuple = (),
        skinEdges: tuple = (),
        stringerEdges: tuple = (),
    ) -> Set:
        """This method creates a set from a sequence of objects in a model database.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].parts[name].Set
                mdb.models[name].rootAssembly.Set

        Parameters
        ----------
        name
            A String specifying the repository key.
        nodes
            A sequence of MeshNode objects. The default value is None.
        elements
            A sequence of MeshElement objects. The default value is None.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying other objects to be included in the set. The default value is
            None.
        vertices
            A sequence of ConstrainedSketchVertex objects. The default value is None.
        edges
            A sequence of Edge objects. The default value is None.
        faces
            A sequence of Face objects. The default value is None.
        cells
            A sequence of Cell objects. The default value is None.
        xVertices
            A sequence of ConstrainedSketchVertex objects that excludes specific vertices from the set. The default
            value is None.
        xEdges
            A sequence of Edge objects that excludes specific edges from the set. The default value
            is None.
        xFaces
            A sequence of Face objects that excludes specific faces from the set. The default value
            is None.
        referencePoints
            A sequence of ReferencePoint objects. The default value is an empty sequence.
        skinFaces
            A tuple of tuples specifying a skin name and the sequence of faces associated with this
            skin. Valid only for geometric regions on 3D and 2D parts.
        skinEdges
            A tuple of tuples specifying a skin name and the sequence of edges associated with this
            skin. Valid only for geometric regions on Axisymmetric parts.
        stringerEdges
            A tuple of tuples specifying a stringer name and the sequence of edges associated with
            this stringer. Valid only for geometric regions on 3D and 2D parts.

        Returns
        -------
        Set
            A :py:class:`~abaqus.Region.Set.Set` object.
        """
        ...

    @typing.overload
    def Set(self, name: str, objectToCopy: Set) -> Set:
        """This method copies a set from an existing set.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].parts[name].Set
                mdb.models[name].rootAssembly.Set

        Parameters
        ----------
        name
            A String specifying the name of the set.
        objectToCopy
            A :py:class:`~abaqus.Region.Set.Set` object to be copied.

        Returns
        -------
        Set
            A :py:class:`~abaqus.Region.Set.Set` object.
        """
        ...

    def Set(self, name, *args, **kwargs) -> Set:
        self.sets[name] = aSet = Set(name, *args, **kwargs)
        return aSet
