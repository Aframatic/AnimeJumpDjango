<?php
$user = Auth::user();
$access = $user->access ?? '0';
?>

@if($access == '2')
    @include('moderator.includes.header')
@elseif($access == '3')
    @include('admin.includes.header')
@else
    @include('includes.header')
@endif

<div class="container">
    <div class="main">

        <div class="main_h1">
            <div class="col align-content-center">
                <h1 class="main_h1_text">Редактирование новости</h1>
            </div>
        </div>

        {{--Вывод новости--}}
        <div class="card shadow border-0 mb-7">
            <div class="table-responsive">
                <form action="{{ route('check_edit_news') }}" method="post">
                    @csrf
                    <input type="hidden" name="id" value="{{$news->id}}">
                    <table class="table table-hover table-nowrap">
                        <thead class="thead-light">
                        <tr>
                            <th scope="col">Название</th>
                            <td><input type="text" class="text" name="name" value="{{$news->name}}"/></td>
                        </tr>
                        <tr>
                            <th scope="col">Картинка</th>
                            <td><label for="img">{{$news->img}}</label>
                                <input id="img" type="file" name="img" accept="image/png, image/jpeg, image/jpg"
                                       value="{{$news->img}}"/>
                            </td>
                        </tr>
                        <tr>
                            <th scope="col">Описание</th>
                            <td><input type="text" class="text" name="description"
                                       value="{{$news->description}}"/>
                            </td>
                        </tr>
                        <tr>
                            <th scope="col">Видео</th>
                            <td><input type="url" class="text" name="video"
                                       value="{{$news->video}}"/>
                            </td>
                        </tr>
                        <tr>
                            <th scope="col">Новость опубликована</th>
                            <td>
                                <select name="publish_at">
                                    @if(empty($news->publish_at))
                                        <option value="">Нет</option>
                                        <option value="{{now()}}">Да</option>
                                    @else
                                        <option value="{{now()}}">Да</option>
                                        <option value="">Нет</option>
                                    @endif
                                </select>
                            </td>
                        </tr>
                        <input type="submit" class="btn btn-sm btn-neutral" value="Сохранить">
                        </thead>
                    </table>
                </form>
                @if ($errors->any())
                    <div class="alert alert-danger mt-2">
                        <ul>
                            @foreach ($errors->all() as $error)
                                <li>{{ $error }}</li>
                            @endforeach
                        </ul>
                    </div>
                @endif
            </div>
        </div>
    </div>
</div>
@include('includes.footer')
