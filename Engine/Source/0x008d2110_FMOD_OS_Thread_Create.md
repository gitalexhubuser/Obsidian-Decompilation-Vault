---
offset: "0x008d2110"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_os_misc.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008d2110 — `FMOD_OS_Thread_Create`

- **Адрес (Offset):** `0x008d2110`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_os_misc.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008d2110
FMOD_RESULT FMOD_OS_Thread_Create(const char *name, THREAD_RETURNTYPE (THREAD_CALLCONV *func)(void *param), void *param, FMOD_THREAD_PRIORITY priority, void *stack, int stacksize, void **handle)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008d2110 в IDA Pro / Ghidra
