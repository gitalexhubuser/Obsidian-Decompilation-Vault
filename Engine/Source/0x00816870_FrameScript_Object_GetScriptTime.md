---
offset: "0x00816870"
module: "Engine/Source"
file: "Engine/Source/FrameScript/FrameScript_Object.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00816870 — `FrameScript_Object_GetScriptTime`

- **Адрес (Offset):** `0x00816870`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/FrameScript/FrameScript_Object.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00816870
void FrameScript_Object::GetScriptTime(lua_State* L, const FrameScript_Object::ScriptIx& script, double* time, uint32_t* calls) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00816870 в IDA Pro / Ghidra
