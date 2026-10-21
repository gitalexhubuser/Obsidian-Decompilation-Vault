---
offset: "0x00767fc0"
module: "Engine/Source"
file: "Engine/Source/ConsoleBase/ConsoleVar.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00767fc0 — `CVar_Register`

- **Адрес (Offset):** `0x00767fc0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ConsoleBase/ConsoleVar.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00767fc0
CVar* CVar::Register(const char* name, const char* help, uint32_t flags, const char* value, bool (*callback)(CVar*, const char*, const char*, void*), uint32_t category, bool setCommand, void* arg, bool unk) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00767fc0 в IDA Pro / Ghidra
