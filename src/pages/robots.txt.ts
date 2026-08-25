export const prerender = true;
export function GET() { return new Response(`User-agent: *\nAllow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n\nUser-agent: ChatGPT-User\nAllow: /\n\nUser-agent: ClaudeBot\nAllow: /\n\nUser-agent: PerplexityBot\nAllow: /\n\nSitemap: https://jonaselgammal.github.io/sitemap.xml\n`, {headers:{'Content-Type':'text/plain; charset=utf-8'}}); }
