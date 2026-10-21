---
offset: "0x004da4b0"
module: "WoW/Source"
file: "WoW/Source/Glue/CGlueMgr.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004da4b0 — `CGlueMgr_SetLoginStateAndResult`

- **Адрес (Offset):** `0x004da4b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Glue/CGlueMgr.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004da4b0
void CGlueMgr::SetLoginStateAndResult(LOGIN_STATE state, LOGIN_RESULT result, const char* addressString, const char* stateString, const char* resultString, uint16_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004da4b0 в IDA Pro / Ghidra
