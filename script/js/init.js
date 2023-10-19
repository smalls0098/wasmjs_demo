// -----------------下面基本不用动，基本都初始化和结束初始化逻辑

// 手动初始化
var tempRet0 = 0;

// async
function init() {
    const imports = __wbg_get_imports();
    __wbg_init_memory(imports);
    imports.env = {
        setTempRet0: function(x) {
            tempRet0 = x;
        },
    }
    const instance = init_func(imports);
    const module = {};
    return __wbg_finalize_init(instance, module);
}

export default init;