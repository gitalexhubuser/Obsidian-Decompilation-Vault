---
offset: "0x004d5c40"
module: "WoW/Source"
file: "WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d5c40 — `ClntObjMgrUnsetTypeMirrorHandler`

- **Адрес (Offset):** `0x004d5c40`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d5c40
void ClntObjMgrUnsetTypeMirrorHandler(OBJECT_TYPE_ID typeId, uint32_t fieldOffset, MIRRORHANDLERFUNC function, void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d5c40 в IDA Pro / Ghidra
