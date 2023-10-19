def main():
    with open("target/pkg/smalls.js", encoding="utf-8") as r:
        content = r.read()
    load_start_pos = content.find("async function __wbg_load")
    load_end_pos = content.find("function __wbg_get_imports()")
    content = content[:load_start_pos] + content[load_end_pos:]

    load_start_pos = content.find("function initSync(module)")
    load_end_pos = content.find("export { initSync }")
    content = content[:load_start_pos] + content[load_end_pos:]

    content = content.replace("__wbg_init.__wbindgen_wasm_module = module;", "")
    content = content.replace("wasm = instance.exports;", "wasm = instance;")
    content = content.replace("export { initSync }", "")
    content = content.replace("export default init;", "")
    content = content.replace("export default __wbg_init;", "")

    with open("script/js/custom_func.js", mode="r", encoding="utf-8") as r:
        custom_func = r.read()
    content += custom_func

    with open("script/js/init.js", mode="r", encoding="utf-8") as r:
        wasm = r.read()
    content += wasm

    content = "import { init_func } from './smalls_bg';\n" + content
    content = "import { TextDecoder, TextEncoder } from './polyfill';\n\n" + content

    with open("target/dist/smalls.js", mode="w") as w:
        w.write(content)

    with open("target/pkg/smalls_bg.js", encoding="utf-8") as r:
        content_bg = r.read()
    content_bg = content_bg.replace("import * as wbg from 'wbg';\n", "")
    content_bg = content_bg.replace("import * as env from 'env';\n", "")
    content_bg = content_bg[:content_bg.find("var retasmFunc")]
    content_bg += "\n\nexport var init_func = asmFunc;"
    with open("target/dist/smalls_bg.js", mode="w") as w:
        w.write(content_bg)

    print("[INFO]: python run ok")


main()
