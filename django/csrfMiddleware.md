1. compare `POST.csrfmiddlewaretoken` and `CSRF_COOKIE` like below:
```
def _compare_salted_tokens(request_csrf_token, csrf_token):
    # Assume both arguments are sanitized -- that is, strings of
    # length CSRF_TOKEN_LENGTH, all CSRF_ALLOWED_CHARS.
    return constant_time_compare(
        _unsalt_cipher_token(request_csrf_token),
        _unsalt_cipher_token(csrf_token),
    )
```
  - what if I know how _sanitize_token work? ==> RSA required?  
  ==> changable secret make `CSRF_COOKIE` changed ==> can I set `CSRF_COOKIE` in `CSRF`?
  - one-time token required? ==> can I set `CSRF_COOKIE` in `CSRF`? 
  - for *safely* like `GET` method, we *can't* have *unsafe* action in views
