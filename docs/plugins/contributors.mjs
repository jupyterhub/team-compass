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

const contributorsDirective = {
  name: 'contributors',
  doc: 'A directive to generate HTML for JupyterHub contributors.',
  alias: ['contrib'],
  arg: { type: String, doc: "Relative path to YAML file", required: true },
  run(data) {
    const yamlPath = data.arg;
    let yamlContent;
    try {
      yamlContent = fs.readFileSync(yamlPath, 'utf8');
    } catch (err) {
      throw new Error(`Cannot read file ${yamlPath}: ${err.message}`);
    }

    const contributors = parseYAML(yamlContent);

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

    return [{ type: "raw", value: `${JSON.stringify(contributors, null, 2)}` }];
  },
};

const plugin = { name: 'contributors', directives: [contributorsDirective] };

export default plugin;

