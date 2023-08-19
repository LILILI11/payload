memo_id = "e5665d5c-155e-4bd1-9fbd-614886078c3c"
if memo_id in Memo.collections:
    secret = Memo.collections[memo_id]
    # 이제 secret를 사용하여 작업을 수행할 수 있습니다.
else:
    print("Memo 객체를 찾을 수 없습니다.")