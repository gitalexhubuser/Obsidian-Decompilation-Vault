---
offset: "0x00769100"
module: "Engine/Source"
file: "Engine/Source/ConsoleBase/ConsoleCommand.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00769100 — `ConsoleCommandRegister`

- **Адрес (Offset):** `0x00769100`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ConsoleBase/ConsoleCommand.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00769100
int32_t ConsoleCommandRegister(const char* command, COMMANDHANDLER handler, CATEGORY category, const char* helpText) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00769100 в IDA Pro / Ghidra
