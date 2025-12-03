import fs from "fs";


function parseYAML(yamlContent) {
  const lines = yamlContent.split("\n");
  const result = [];
  let current = null;
  let currentKey = null;

  for (let line of lines) {
    line = line.trim();
    if (line === "") continue;

    if (line.startsWith("- ")) {
      if (current) result.push(current);
      current = {};
      const rest = line.slice(2).trim();
      if (rest) {
        const [key, ...valueParts] = rest.split(":");
        if (valueParts.length) {
          current[key.trim()] = valueParts.join(":").trim();
        }
      }
    } else if (line.startsWith("-")) {
      if (currentKey && Array.isArray(current[currentKey])) {
        current[currentKey].push(line.slice(1).trim());
      }
    } else if (line.includes(":")) {
      const [key, ...valueParts] = line.split(":");
      const value = valueParts.join(":").trim();
      if (value === "") {
        currentKey = key.trim();
        current[currentKey] = [];
      } else {
        current[key.trim()] = value;
        currentKey = null;
      }
    }
  }
  if (current) result.push(current);
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
      return `  <li>${inner}</li>`;
    }).join("\n")}
    </ul>`;

    return [{ type: "html", value: output }];
  },
};

const plugin = { name: 'contributors', directives: [contributorsDirective] };

export default plugin;

