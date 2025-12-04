import fs from "fs";


function parseYAML(yamlContent) {
  const lines = yamlContent.split("\n");
  const result = [];
  let current = {};
  let currentKey = null;
  let currentValue = null;

  for (let rawLine of lines) {
    const line = rawLine.trim();
    if (line === "" || line.startsWith("#")) {
      continue;
    } else if (line.startsWith("- name:")) {
      if (Object.keys(current).length !== 0) result.push(current);
      current = {};
    }
    // Handle nested list of teams
    if (line.includes("teams:")) {
      currentKey = "teams";
      current[currentKey] = [];
      continue;
    } else if (line.startsWith("-") && !line.includes(":") &&  currentKey === "teams") {
      current["teams"].push(line.replace("-", "").trim());
    } else {
      currentKey = line.split(":")[0].replace("-", "").trim();
      currentValue = line.split(":")[1];
      current[currentKey] = currentValue;
    }
  }
  return result;
}


function renderList(contributors) {
  const output = `<ul>
  ${contributors.map(item => {
    const inner = Object.entries(item)
      .map(([k,v]) => {
        if (Array.isArray(v)) return `<strong>${k}:</strong> ${v.join(", ")}`;
        else return `<strong>${k}:</strong> ${v}`;
      })
      .join("\n");
    return `<li>${inner}</li>`;
  }).join("\n")}
  </ul>`;
  return output;
}


function renderText(contributors) {
  const output = `<p>${contributors.map(item => {
    const name = item.name || "Unknown";
    const handle = item.handle.replace(/"/g, '').trim();
    return `${name} (<a href=https://github.com/${handle}>@${handle}</a>)`;
  })}.</p>`;
  return output;
}


const contributorsDirective = {
  name: 'contributors',
  doc: 'A directive to generate HTML for JupyterHub contributors.',
  alias: ['contrib'],
  arg: { type: String, doc: "Relative path to YAML file", required: true },
  options: {
    render: { type: String, doc: "Type of rendering: 'cards' or 'text'", default: "text" },
  },
  run(data) {
    const yamlPath = data.arg;
    let yamlContent;
    try {
      yamlContent = fs.readFileSync(yamlPath, 'utf8');
    } catch (err) {
      throw new Error(`Cannot read file ${yamlPath}: ${err.message}`);
    }

    const contributors = parseYAML(yamlContent);

    let output;
    if (data.options.render === 'list') {
      output = renderList(contributors);
    } else if (data.options.render === 'text') {
      output = renderText(contributors);
    } else {
      throw new Error(`Unknown render option: ${data.options.render}`);
    }

    return [{ type: "html", value: output }];
  },
};

const plugin = { name: 'contributors', directives: [contributorsDirective] };

export default plugin;

