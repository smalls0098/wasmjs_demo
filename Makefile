.PHONY: wasm
wasm:
	cargo fmt && \
	wasm-pack build --release --no-pack --no-typescript --target web --out-dir target/pkg

.PHONY: wasm-dist
wasm-dist:
	make wasm && \
	rm -rf target/dist && \
	mkdir target/dist && \
    wasm-opt -Oz --strip-debug -o target/pkg/smalls_bg_1.wasm target/pkg/smalls_bg.wasm && \
    wasm2js -O4 --strip-debug --optimize-level=3 --shrink-level=2 -o target/pkg/smalls_bg.js target/pkg/smalls_bg_1.wasm && \
    python3 script/wasm.py && \
	cp script/js/polyfill.js target/dist && \
	javascript-obfuscator --config script/obs.json target/dist/polyfill.js && \
	javascript-obfuscator --config script/obs.json target/dist/smalls.js && \
	javascript-obfuscator --config script/obs.json target/dist/smalls_bg.js
