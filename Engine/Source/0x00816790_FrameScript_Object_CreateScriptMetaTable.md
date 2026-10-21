---
offset: "0x00816790"
module: "Engine/Source"
file: "Engine/Source/FrameScript/FrameScript_Object.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00816790 — `FrameScript_Object_CreateScriptMetaTable`

- **Адрес (Offset):** `0x00816790`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/FrameScript/FrameScript_Object.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00816790
int32_t FrameScript_Object::CreateScriptMetaTable(lua_State* L, void (*registerFunc)(lua_State*)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00816790 в IDA Pro / Ghidra
