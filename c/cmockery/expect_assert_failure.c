/* -*- coding:utf-8; -*- */
#include <assert.h>
#include <stdbool.h>

#include <setjmp.h>
#include <stdarg.h>
#include <stddef.h>

#include <google/cmockery.h> /* 注意该头文件依赖上面三个头文件，注意顺序 */

#if UNIT_TESTING
extern void mock_assert (const int result, const char *const expression,
                         const char *const file, const int line);
#undef assert
#define assert(expression) \
    mock_assert ((int)(expression), #expression, __FILE__, __LINE__);
#endif  // UNIT_TESTING

void f () {}
void g () { assert (true); }
void h () { assert (false); }

void test_success (void **state) { expect_assert_failure (f); }
void test_failure (void **state) { expect_assert_failure (g); }
void test_failure_2 (void **state) { expect_assert_failure (h); }

int main (int argc, char *argv[]) {
    const UnitTest tests[] = {
        unit_test (test_success),
        unit_test (test_failure),
        unit_test (test_failure_2),
    };
    return run_tests (tests);
}
