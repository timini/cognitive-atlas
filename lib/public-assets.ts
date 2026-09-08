/** Public research URLs work at both the domain root and a Pages project path. */
declare const __ATLAS_PUBLIC_BASE_PATH__: string;

export function publicAsset(path: string, basePath = typeof __ATLAS_PUBLIC_BASE_PATH__ === 'undefined' ? '' : __ATLAS_PUBLIC_BASE_PATH__): string {
  return `${basePath.replace(/\/$/, '')}/${path.replace(/^\/+/, '')}`;
}
