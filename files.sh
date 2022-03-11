cat << EOF > erlang.txt
"""
    % Quick sort

    -module (recursion).
    -export ([qsort/1]).

    qsort([]) -> [];
    qsort([Pivot|T]) ->
          qsort([X || X <- T, X < Pivot])
          ++ [Pivot] ++
          qsort([X || X <- T, X >= Pivot]).
"""
EOF
echo "done"