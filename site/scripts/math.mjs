import katex from 'katex';
const esc=value=>String(value).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
export const diagnostics={mathCount:0,mathErrors:[],mathWarnings:[]};
function mathHtml(tex, display, context) {
  diagnostics.mathCount++;
  try {
    const html = katex.renderToString(tex, { displayMode: display, throwOnError: true, trust: false, output: 'htmlAndMathml', strict: (code, message) => { diagnostics.mathWarnings.push({ doc: context.id, code, message }); return 'ignore'; } });
    return display ? `<div class="math-display">${html}</div>\n` : html;
  } catch (error) {
    diagnostics.mathErrors.push({ doc: context.id, tex, message: error.message });
    return `<span class="math-error">${esc(tex)}</span>`;
  }
}
function mathExtensions(context) {
  return [
    { name: 'vciMathBlock', level: 'block', start: src => src.search(/(?:^|\n)[ \t]*(?:\$\$|\\\[)/), tokenizer(src) {
      const m = /^(?: {0,3})\$\$[ \t]*\n?([\s\S]*?)\n?\$\$[ \t]*(?:\n|$)/.exec(src) || /^(?: {0,3})\\\[\s*\n?([\s\S]*?)\\\][ \t]*(?:\n|$)/.exec(src);
      if (m) return { type: 'vciMathBlock', raw: m[0], text: m[1].trim() };
    }, renderer(token) { return mathHtml(token.text, true, context); } },
    { name: 'vciMathInline', level: 'inline', start: src => src.search(/\$|\\\(/), tokenizer(src) {
      const m = /^\$(?!\$)((?:\\.|[^\n$])+?)\$(?!\$)/.exec(src) || /^\\\(([\s\S]+?)\\\)/.exec(src);
      if (m) return { type: 'vciMathInline', raw: m[0], text: m[1].trim() };
    }, renderer(token) { return mathHtml(token.text, false, context); } }
  ];
}

export {mathExtensions};
