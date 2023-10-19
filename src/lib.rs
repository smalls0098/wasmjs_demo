use wasm_bindgen::prelude::wasm_bindgen;

// 结论，返回值尽量用String
#[wasm_bindgen]
pub struct MR {
    status: bool,
    data: String,
}

#[wasm_bindgen]
impl MR {
    fn err() -> MR {
        return MR {
            status: false,
            data: "".to_string(),
        };
    }
    #[wasm_bindgen(getter)]
    pub fn status(&self) -> bool {
        self.status
    }
    #[wasm_bindgen(getter)]
    pub fn data(&self) -> String {
        self.data.clone()
    }
}

#[wasm_bindgen]
pub fn sign(data: String) -> MR {
    return MR { status: true, data };
}
