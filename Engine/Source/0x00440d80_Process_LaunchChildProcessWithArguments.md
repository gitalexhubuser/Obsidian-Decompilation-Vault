---
offset: "0x00440d80"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Process/Win64/Process.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00440d80 — `Process_LaunchChildProcessWithArguments`

- **Адрес (Offset):** `0x00440d80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Process/Win64/Process.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00440d80
bool Blizzard::Process::LaunchChildProcessWithArguments(const char* path, const char* arguments, void (*callback)(void*), void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00440d80 в IDA Pro / Ghidra
