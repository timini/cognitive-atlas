import type { NextConfig } from 'next';

const githubPages = process.env.ATLAS_HOSTING_TARGET === 'github-pages';
const nextConfig: NextConfig = githubPages ? {
  output: 'export',
  basePath: process.env.ATLAS_PAGES_BASE_PATH ?? '/cognitive-atlas',
  trailingSlash: true,
} : {};

export default nextConfig;
