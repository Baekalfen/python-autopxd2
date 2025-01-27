import os

BUILTIN_HEADERS_DIR = os.path.join(os.path.dirname(__file__), "include")

# Stubs for MacOSX.sdk/usr/include
DARWIN_HEADERS_DIR = os.path.join(os.path.dirname(__file__), "darwin-include")

# Types declared by pycparser fake headers that we should ignore
IGNORE_DECLARATIONS = {
    "size_t",
    "__builtin_va_list",
    "__gnuc_va_list",
    "__int8_t",
    "__uint8_t",
    "__int16_t",
    "__uint16_t",
    "__int_least16_t",
    "__uint_least16_t",
    "__int32_t",
    "__uint32_t",
    "__int64_t",
    "__uint64_t",
    "__int_least32_t",
    "__uint_least32_t",
    "__s8",
    "__u8",
    "__s16",
    "__u16",
    "__s32",
    "__u32",
    "__s64",
    "__u64",
    "_LOCK_T",
    "_LOCK_RECURSIVE_T",
    "_off_t",
    "__dev_t",
    "__uid_t",
    "__gid_t",
    "_off64_t",
    "_fpos_t",
    "_ssize_t",
    "wint_t",
    "_mbstate_t",
    "_flock_t",
    "_iconv_t",
    "__ULong",
    "__FILE",
    "ptrdiff_t",
    "wchar_t",
    "__off_t",
    "__pid_t",
    "__loff_t",
    "u_char",
    "u_short",
    "u_int",
    "u_long",
    "ushort",
    "uint",
    "clock_t",
    "time_t",
    "daddr_t",
    "caddr_t",
    "ino_t",
    "off_t",
    "dev_t",
    "uid_t",
    "gid_t",
    "pid_t",
    "key_t",
    "ssize_t",
    "mode_t",
    "nlink_t",
    "fd_mask",
    "_types_fd_set",
    "clockid_t",
    "timer_t",
    "useconds_t",
    "suseconds_t",
    "FILE",
    "fpos_t",
    "cookie_read_function_t",
    "cookie_write_function_t",
    "cookie_seek_function_t",
    "cookie_close_function_t",
    "cookie_io_functions_t",
    "div_t",
    "ldiv_t",
    "lldiv_t",
    "sigset_t",
    "__sigset_t",
    "_sig_func_ptr",
    "sig_atomic_t",
    "__tzrule_type",
    "__tzinfo_type",
    "mbstate_t",
    "sem_t",
    "pthread_t",
    "pthread_attr_t",
    "pthread_mutex_t",
    "pthread_mutexattr_t",
    "pthread_cond_t",
    "pthread_condattr_t",
    "pthread_key_t",
    "pthread_once_t",
    "pthread_rwlock_t",
    "pthread_rwlockattr_t",
    "pthread_spinlock_t",
    "pthread_barrier_t",
    "pthread_barrierattr_t",
    "jmp_buf",
    "rlim_t",
    "sa_family_t",
    "sigjmp_buf",
    "stack_t",
    "siginfo_t",
    "z_stream",
    "int8_t",
    "uint8_t",
    "int16_t",
    "uint16_t",
    "int32_t",
    "uint32_t",
    "int64_t",
    "uint64_t",
    "int_least8_t",
    "uint_least8_t",
    "int_least16_t",
    "uint_least16_t",
    "int_least32_t",
    "uint_least32_t",
    "int_least64_t",
    "uint_least64_t",
    "int_fast8_t",
    "uint_fast8_t",
    "int_fast16_t",
    "uint_fast16_t",
    "int_fast32_t",
    "uint_fast32_t",
    "int_fast64_t",
    "uint_fast64_t",
    "intptr_t",
    "uintptr_t",
    "intmax_t",
    "uintmax_t",
    "bool",
    "va_list",
}

STDINT_DECLARATIONS = {
    "int8_t",
    "uint8_t",
    "int16_t",
    "uint16_t",
    "int32_t",
    "uint32_t",
    "int64_t",
    "uint64_t",
    "int_least8_t",
    "uint_least8_t",
    "int_least16_t",
    "uint_least16_t",
    "int_least32_t",
    "uint_least32_t",
    "int_least64_t",
    "uint_least64_t",
    "int_fast8_t",
    "uint_fast8_t",
    "int_fast16_t",
    "uint_fast16_t",
    "int_fast32_t",
    "uint_fast32_t",
    "int_fast64_t",
    "uint_fast64_t",
    "intptr_t",
    "uintptr_t",
    "intmax_t",
    "uintmax_t",
}
