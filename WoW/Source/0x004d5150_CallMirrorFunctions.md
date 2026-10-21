---
offset: "0x004d5150"
module: "WoW/Source"
file: "WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d5150 — `CallMirrorFunctions`

- **Адрес (Offset):** `0x004d5150`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d5150
static void CallMirrorFunctions(TSExplicitList<CMirrorHandler, offsetof(CMirrorHandler, m_link2)>* pending, WOWGUID guid, CGObject_C* object, OBJECT_TYPE_ID typeId) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d5150 в IDA Pro / Ghidra
