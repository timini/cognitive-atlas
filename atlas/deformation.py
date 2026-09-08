"""Continuous piecewise-affine deformation in an explicitly labeled equirectangular view.

Boundary pins remain fixed. Foldovers are measured, never claimed topology-preserving.
This interpolation is a visualization, not a reconstruction of country shapes.
"""
import numpy as np
from scipy.spatial import Delaunay


def projected(latlon):
    latlon = np.asarray(latlon)
    return np.column_stack([latlon[:, 1], -latlon[:, 0]])


def mesh(source_latlon, target_latlon):
    source, target = projected(source_latlon), projected(target_latlon)
    # Select nearest longitude branch for each displacement.
    target[:, 0] = source[:, 0] + (target[:, 0] - source[:, 0] + 180) % 360 - 180
    border = np.array([[x, y] for x in np.linspace(-180, 180, 13) for y in [-90, 90]] +
                      [[x, y] for x in [-180, 180] for y in np.linspace(-75, 75, 11)])
    src = np.vstack([source, border])
    dst = np.vstack([target, border])
    tri = Delaunay(src)
    a, b = src[tri.simplices], dst[tri.simplices]
    def area(t):
        u, v = t[:, 1] - t[:, 0], t[:, 2] - t[:, 0]
        return u[:, 0] * v[:, 1] - u[:, 1] * v[:, 0]
    folds = int((area(a) * area(b) <= 0).sum())
    return {"source": src.tolist(), "target": dst.tolist(), "triangles": tri.simplices.tolist(),
            "foldovers": folds, "projection": "equirectangular",
            "boundary_policy": "fixed frame pins; nearest longitude branch",
            "warning": "Country outlines are illustrative interpolation; folds may occur"}


def warp_points(points, control_mesh):
    src, dst = np.asarray(control_mesh["source"]), np.asarray(control_mesh["target"])
    tri = Delaunay(src)
    points = np.asarray(points)
    simplex = tri.find_simplex(points)
    result = points.copy()
    inside = simplex >= 0
    s = simplex[inside]
    bary = np.einsum("ijk,ik->ij", tri.transform[s, :2], points[inside] - tri.transform[s, 2])
    weights = np.column_stack([bary, 1 - bary.sum(axis=1)])
    result[inside] = np.einsum("ij,ijk->ik", weights, dst[tri.simplices[s]])
    return result
