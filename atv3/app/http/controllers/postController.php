use App\Post;

public function index()
{
    return Post::all();
}

public function store(Request $request)
{
    $post = new Post();
    $post->title = $request->input('title');
    $post->body = $request->input('body');
    $post->save();

    return response()->json($post, 201);
}

public function show($id)
{
    return Post::find($id);
}

public function update(Request $request, $id)
{
    $post = Post::find($id);
    $post->title = $request->input('title');
    $post->body = $request->input('body');
    $post->save();

    return response()->json($post, 200);
}

public function destroy($id)
{
    $post = Post::find($id);
    $post->delete();

    return response()->json(null, 204);
}
